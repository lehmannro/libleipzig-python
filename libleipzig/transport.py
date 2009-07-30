# Copyright (C) 2009 Robert Lehmann

import functools
import inspect
import suds

BASEURL = 'http://pcai055.informatik.uni-leipzig.de:8100/axis/services/%s?wsdl'

def service(*result_types):
    def wrapper(f):
        name = f.__name__
        args, _, _, _ = inspect.getargspec(f)
        auth = suds.transport.http.HttpAuthenticated(
               username='anonymous', password='anonymous')
        # this prefetches the WSDL on library load!
        client = suds.client.Client(BASEURL % name, transport=auth)

        @functools.wraps(f)
        def func(word, *vectors):
            if len(args) - 1 != len(vectors):
                raise TypeError("service `%s' got %d arguments, expects %d (%s)" %
                    (name, len(vectors)+1, len(args), ", ".join(args)))

            # assemble query to the SOAP service
            request = client.factory.create('RequestParameter')
            request.corpus = 'de'

            for key, value in zip(args, (word,) + vectors):
                vector = client.factory.create('ns0:DataVector')

                key_row = client.factory.create('ns0:dataRow')
                key_row.value = key
                vector.dataRow.append(key_row)

                value_row = client.factory.create('ns0:dataRow')
                value_row.value = value
                vector.dataRow.append(value_row)

                request.parameters.dataVectors.append(vector)

            response = client.service.execute(request)
            for e in response.result.dataVectors:
                yield dict(zip(result_types, e.dataRow))

        return func
    return wrapper
