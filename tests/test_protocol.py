# Copyright (C) 2009 Robert Lehmann

import libleipzig

def test_services():
    assert hasattr(libleipzig, 'services')
    s = libleipzig.services
    assert isinstance(s, dict)
    assert s
    name, func = s.iteritems().next()
    assert isinstance(name, basestring)
    assert callable(func)
