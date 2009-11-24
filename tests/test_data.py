# Copyright (C) 2009 Robert Lehmann
# encoding: utf-8
#
# extremely fragile tests due to their dependency on an external database

from nose.tools import assert_raises
from libleipzig import *

def test_baseform_schlange():
    result = Baseform("Schlangen")
    assert len(result) == 2
    singular, plural = result

    assert singular == ("Schlange", "N")
    assert singular[0] == singular.Grundform
    assert singular[1] == singular.Wortart

    assert plural == ("Schlangen", "S")

def test_encoding():
    # encoding request and result
    assert Baseform(u"schlängeln") == [(u"schlängeln", "V")]
    assert Baseform(u"€") == [] # do not blow up at least

def test_empty():
    assert Baseform("foobarbaz") == []
