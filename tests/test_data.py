# Copyright (C) 2009 Robert Lehmann
#
# extremely fragile tests due to their dependency on an external database

from libleipzig import *

# -    print list(Synonyms('Python', 3))
# -    print list(Similarity('Python', 3))
# -    print list(Kreuzwortraetsel('Py%%on', 6, 4))
def test_baseform_schlange():
    result = list(Baseform("Schlangen"))
    assert len(result) == 2
    singular, plural = result

    assert isinstance(singular, tuple)
    assert isinstance(plural, tuple)

    assert len(singular) == 2
    assert singular == ("Schlange", "N")
    assert isinstance(singular[0], basestring)
    assert hasattr(singular, 'Grundform')
    assert hasattr(singular, 'Wortart')
    assert singular[0] == singular.Grundform
    assert singular[1] == singular.Wortart
    
    assert plural == ("Schlangen", "S")
