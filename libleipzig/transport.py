# Copyright (C) 2009, 2010 Robert Lehmann

import functools
import inspect
import operator
import suds

BASEURL = 'http://pcai055.informatik.uni-leipzig.de:8100/axis/services/%s?wsdl'
services = {}

def service(*results):
    def wrapper(f):
        name = f.__name__
        args, _, _, _ = inspect.getargspec(f)

        # Exposing `client.options.cache.clear` is not sensible since suds
        # caches only for inter-session performance. Clearing it has no
        # runtime impact on the library as the *real* cache is the client
        # object keeping parsed WSDL definitions.

        auth = suds.transport.http.HttpAuthenticated(
               username='anonymous', password='anonymous')

        class Result(tuple): # poor man's namedtuple
            def __repr__(self):
                return "(%s)" % ", ".join(
                        "%s: %s" % d for d in zip(results, map(repr, self)))
        for n, typ in enumerate(results):
            setattr(Result, typ, property(operator.itemgetter(n)))
        Result.__name__ = "%sResult" % name

        def get_client(func, name):
            if not hasattr(func, '_client'):
                func._client = client = suds.client.Client(BASEURL % name,
                        transport=auth)
                client.options.cache.setduration(days=0)
            return func._client

        @functools.wraps(f)
        def func(*vectors):
            # this prefetches the WSDL on library load!
            client = get_client(func, name)

            if len(args) != len(vectors):
                raise TypeError(
                    "service `%s' got %d arguments, expects %d (%s)" %
                    (name, len(vectors), len(args), ", ".join(args)))

            # assemble query to the SOAP service
            request = client.factory.create('RequestParameter')
            request.corpus = 'de'

            for key, value in zip(args, vectors):
                vector = client.factory.create('ns0:DataVector')

                key_row = client.factory.create('ns0:dataRow')
                key_row.set(key)
                vector.dataRow.append(key_row)

                value_row = client.factory.create('ns0:dataRow')
                value_row.set(value)
                vector.dataRow.append(value_row)

                request.parameters.dataVectors.append(vector)

            # fire query and construct result tuples
            response = client.service.execute(request)
            if not response.result:
                return []
            # do not use yield to trigger function body immediately
            return [Result(map(unicode, e.dataRow))
                    for e in response.result.dataVectors]

        func._doc = func.__doc__ or ''
        func._args = args
        func._returns = results
        func.__doc__ = "%s(%s) -> %s\n" % (name, ", ".join(args),
            ", ".join(results)) + func._doc
        func.prefetch = lambda: get_client(func, name)
        services[name] = func

        return func
    return wrapper
