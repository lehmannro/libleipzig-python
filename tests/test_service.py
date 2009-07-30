# Copyright (C) 2009 Robert Lehmann

from nose.tools import *
from libleipzig import *

def test_doc():
    assert hasattr(Baseform, '__doc__')
    assert isinstance(Baseform.__doc__, basestring)

    lines = Baseform.__doc__.splitlines()
    assert len(lines) > 1 # automatically generated + service description

def test_args():
    assert_raises(TypeError, Baseform)
    assert_raises(TypeError, Baseform, "Schlange", 42)

def test_wrapped():
    assert Baseform.__name__ == 'Baseform'
    assert Baseform.__module__ == 'libleipzig.protocol'
