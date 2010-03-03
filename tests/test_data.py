# Copyright (C) 2009, 2010 Robert Lehmann
# encoding: utf-8
#
# extremely fragile tests due to their dependency on an external database

from nose.tools import assert_raises
from libleipzig import *

def test_baseform_schlange():
    result = Baseform(u"Schlangen")
    assert len(result) == 2
    singular, plural = result

    assert singular == (u"Schlange", u"N")
    assert singular[0] == singular.Grundform
    assert singular[1] == singular.Wortart

    assert plural == (u"Schlangen", u"S")

def test_encoding():
    # encoding request and result
    assert Baseform(u"schlängeln") == [(u"schlängeln", u"V")]
    assert Baseform(u"€") == [] # do not blow up at least

def test_empty():
    assert Baseform(u"foobarbaz") == []

def test_repr():
    printable = repr(Baseform(u"schlängeln"))
    assert printable == r"[(Grundform: u'schl\xe4ngeln', Wortart: u'V')]"
