from libleipzig.transport import services
from libleipzig import WebFault
import optparse

parser = optparse.OptionParser()
parser.add_option("-s", "--schema", action='store_true',
    help="show service's output schema and exit")
parser.add_option("-d", "--delimiter", metavar="DELIM", default=",",
    help="use DELIM instead of comma for field delimiter")
parser.add_option("-u", "--user",
    help="auth with USER (requires -p)")
parser.add_option("-p", "--password", metavar="PASS",
    help="auth with PASS (requires -u)")
parser.add_option("-v", "--verbose", action='store_true',
    help="enable SOAP debugging output on failure")

def main():
    import sys
    options, args = parser.parse_args()
    if not args:
        parser.print_help()
        return 1
    if args[0] not in services:
        print >>sys.stderr, "unknown service"
        return 1
    service, args = services[args[0]], args[1:]
    delim = options.delimiter.decode('string-escape')
    if options.schema:
        print delim.join(service._returns)
        return

    if options.user and options.password:
        #XXX fail if only one is given
        service.set_credentials(options.user, options.password)

    import logging
    if options.verbose:
        h = logging.StreamHandler(sys.stderr)
    else:
        class NullHandler(logging.Handler):
            def emit(self, record):
                pass
        h = NullHandler()
    logging.getLogger('suds.client').addHandler(h)

    try:
        results = service(*args)
    except TypeError, e:
        print >>sys.stderr, str(e)
        return 1
    except WebFault, e:
        print >>sys.stderr, "remote failure: %s" % e
        return 2
    else:
        print '\n'.join(delim.join(result) for result in results)

if __name__ == '__main__':
    main()
