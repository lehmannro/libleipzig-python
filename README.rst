=====================================================
 libleipzig -- wortschatz.uni-leipzig.de binding
=====================================================

**libleipzig-python** provides a wrapper to the web services provided by the
`Deutscher Wortschatz`_ project of the University of Leipzig. It currently
supports all level 1 service calls (unauthenticated). See the file
``libleipzig/protocol.py`` or ``libleipzig.services`` for details.

.. _Deutscher Wortschatz: http://wortschatz.uni-leipzig.de/

.. attention:: libleipzig prefetches all service interfaces on initial load.
   This process requires an Internet connection.


>>> from libleipzig import *
>>> r = list(Baseform("Schlangen"))
>>> r
[(Grundform: Schlange, Wortart: N), (Grundform: Schlangen, Wortart: S)]
>>> r[0].Grundform
'Schlange'
>>> print Baseform.__doc__.splitlines()[0]
Baseform(Wort) -> Grundform, Wortart
>>>

Dependencies
------------

- suds_ 0.3.7 beta or higher

.. _suds: https://fedorahosted.org/suds/#Resources
