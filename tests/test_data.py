# Copyright (C) 2009, 2010 Robert Lehmann
# encoding: utf-8
#
# extremely fragile tests due to their dependency on an external database

import os
from nose.tools import assert_raises
from nose.exc import SkipTest
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

def test_other_corpus():
    assert RightNeighbours(u"snake", 1, corpus='en')

def test_invalid_corpus():
    assert_raises(WebFault, Baseform, u"foobar", corpus='invalid')

def test_auth():
    assert RightNeighbours(u"Schlange", 1, auth=("anonymous", "anonymous"))

def test_invalid_auth():
    assert_raises(WebFault, RightNeighbours, u"Schlange", 1,
        auth=("invalid", "auth"))

def test_level_2():
    # export LIBLEIPZIGAUTH=username:password
    if 'LIBLEIPZIGAUTH' not in os.environ:
        raise SkipTest
    auth = os.environ['LIBLEIPZIGAUTH'].split(":")
    assert RightNeighbours(u"Schlange", 1, auth=auth)

def test_auth_setting_level_2():
    # export LIBLEIPZIGAUTH=username:password
    if 'LIBLEIPZIGAUTH' not in os.environ:
        raise SkipTest
    auth = os.environ['LIBLEIPZIGAUTH'].split(":")
    LeftNeighbours.set_credentials(*auth)
    assert LeftNeighbours(u"Schlange", 1)


def test_auth_setting_invalid():
    Synonyms.set_credentials("invalid", "auth")
    assert_raises(WebFault, Synonyms, u"Schlange", 1)
    # persists along multiple calls
    assert_raises(WebFault, Synonyms, u"Schlange", 1)
    # others are unaffected
    test_baseform_schlange()
