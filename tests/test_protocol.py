# Copyright (C) 2009 Robert Lehmann

import os
import tempfile
import libleipzig

def test_services():
    s = libleipzig.services
    assert 'Baseform' in s
    name, func = s.iteritems().next()
    assert isinstance(name, basestring)
    assert callable(func)

def test_cache():
    assert os.listdir(os.path.join(tempfile.gettempdir(), "suds"))
