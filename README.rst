=================================================
 libleipzig -- wortschatz.uni-leipzig.de binding
=================================================

**libleipzig-python** provides a wrapper to the web services provided by the
`Deutscher Wortschatz`_ project of the University of Leipzig. It currently
supports all public service calls. These do not require authentication.

.. _Deutscher Wortschatz: http://wortschatz.uni-leipzig.de/

.. contents:: Table of Contents

.. attention:: libleipzig prefetches *all* service interfaces on initial load.
   This process requires an Internet connection.

   Subsequent ``import``\ s use indefinitely cached definitions (WSDL files).


Example
-------

>>> from libleipzig import * # might take some time initially
>>> r = list(Baseform("Schlangen"))
>>> r
[(Grundform: Schlange, Wortart: N), (Grundform: Schlangen, Wortart: S)]
>>> r[0].Grundform
'Schlange'
>>> help(Baseform) # doctest: +NORMALIZE_WHITESPACE
Help on function Baseform in module libleipzig.protocol:
Baseform(word, *vectors)
    Baseform(Wort) -> Grundform, Wortart
        Return the lemmatized (base) form.
>>>

.. **

Dependencies
------------

- Python 2.5 or later 2.x releases
- suds_ 0.3.7 beta (r537) or later

.. _suds: https://fedorahosted.org/suds/#Resources
