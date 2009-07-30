# Copyright (C) 2009 Robert Lehmann

import suds
from libleipzig import protocol

BASEURL = 'http://pcai055.informatik.uni-leipzig.de:8100/axis/services/%s?wsdl'
_PUBLIC = suds.transport.http.HttpAuthenticated(
          username='anonymous', password='anonymous')

def request(service, *args, **kwargs):
    """

    :Parameters:
    - `service`: the name of the executed SOAP method
    - `word`: the term to look up
    Depending on `service` there might be additional arguments expected.

    :Keywords:
    - `auth`: a tuple of auth information (username, password); anonymous
      login if None.

    """
    # determine service
    if service not in protocol.services:
        raise LookupError("service `%s' is not known" % service)
    in_, out = protocol.services[service]
    if len(in_) != len(args):
        raise TypeError("service `%s' got %d arguments, expects %d (%s)" %
            (service, len(args), len(in_), ", ".join(in_)))

    # connect to the SOAP service
    if 'auth' in kwargs:
        auth = suds.transport.http.HttpAuthenticated(dict(zip(
            ('username', 'password'), kwargs['auth'])))
    else:
        auth = _PUBLIC
    client = suds.client.Client(BASEURL % service, transport=auth)

    request = client.factory.create('RequestParameter')
    request.corpus = 'de'

    for key, value in zip(in_, args):
        vector = client.factory.create('ns0:DataVector')

        key_row = client.factory.create('ns0:dataRow')
        key_row.value = key
        vector.dataRow.append(key_row)

        value_row = client.factory.create('ns0:dataRow')
        value_row.value = value
        vector.dataRow.append(value_row)

        request.parameters.dataVectors.append(vector)
    
    response = client.service.execute(request)
    print response
    for e in response.result.dataVectors:
        yield dict(zip(out, e.dataRow))
