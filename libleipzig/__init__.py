# Copyright (C) 2009 Robert Lehmann

__author__ = "Robert Lehmann <libleipzig@robertlehmann.de>"

from libleipzig.protocol import *

if __name__ == '__main__':
    print list(Baseform('Schlangen'))[0].Grundform
    print list(Synonyms('Python', 3))
    print list(Similarity('Python', 10))
