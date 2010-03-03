# Copyright (C) 2009, 2010 Robert Lehmann

from nose.tools import assert_raises
from libleipzig import Baseform, Thesaurus

def test_doc():
    lines = Baseform.__doc__.splitlines()
    assert len(lines) > 1 # automatically generated + service description
    assert len(Baseform._args) == 1
    assert len(Baseform._returns) == 2
    assert Baseform._doc

def test_args():
    assert_raises(TypeError, Baseform)
    assert_raises(TypeError, Baseform, "Schlange", 42)

def test_wrapped():
    assert Baseform.__name__ == 'Baseform'
    assert Baseform.__module__ == 'libleipzig.protocol'

def test_prefetch():
    Thesaurus._client = None
    del Thesaurus._client
    Thesaurus.prefetch()
    assert hasattr(Thesaurus, '_client')
