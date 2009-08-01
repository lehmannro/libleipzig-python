# Copyright (C) 2009 Robert Lehmann
#
# extremely fragile tests due to their dependency on an external database

from libleipzig import *

def test_baseform_schlange():
    result = list(Baseform("Schlangen"))
    assert len(result) == 2
    singular, plural = result

    assert singular == ("Schlange", "N")
    assert singular[0] == singular.Grundform
    assert singular[1] == singular.Wortart
    
    assert plural == ("Schlangen", "S")
