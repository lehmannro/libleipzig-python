from libleipzig.transport import services
from libleipzig import WebFault
import optparse

parser = optparse.OptionParser()
parser.add_option("-s", "--schema", action='store_true',
    help="show service's output schema and exit")
parser.add_option("-d", "--delimiter", metavar="DELIM", default=",",
    help="use DELIM instead of comma for field delimiter")

def main():
    options, args = parser.parse_args()
    if not args or args[0] not in services:
        return parser.exit(1, "unknown service")
    service, args = services[args[0]], args[1:]
    delim = options.delimiter.decode('string-escape')
    if options.schema:
        print delim.join(service._returns)
        return

    try:
        results = service(*args)
    except TypeError, e:
        print str(e)
        return 1
    except WebFault, e:
        print "remote failure: %s" % e
        return 2
    else:
        print '\n'.join(delim.join(result) for result in results)
