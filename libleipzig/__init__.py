# Copyright (C) 2009 Robert Lehmann

__author__ = "Robert Lehmann <libleipzig@robertlehmann.de>"

from libleipzig.transport import request
from libleipzig.protocol import services

if __name__ == '__main__':
    print list(request('Baseform', 'Python'))
