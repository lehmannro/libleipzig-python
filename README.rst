=================================================
 libleipzig -- wortschatz.uni-leipzig.de binding
=================================================

**libleipzig-python** provides a wrapper to the web services provided by the
`Deutscher Wortschatz`_ project of the University of Leipzig. **Deutscher
Wortschatz** is a German database of text corpora and can be utilized to
analyze and contextualize words in the thesaurus. *libleipzig* currently
supports all public service calls. These do not require authentication and are
provided `free of charge`_ for private or scientific purposes.

.. _Deutscher Wortschatz: http://wortschatz.uni-leipzig.de/
.. _free of charge: http://wortschatz.uni-leipzig.de/use.html

.. contents::

.. attention:: libleipzig prefetches__ *all* service interfaces on initial load.
   This process requires an Internet connection.

   Subsequent ``import``\ s use indefinitely cached definitions (WSDL files).

   __ https://fedorahosted.org/suds/wiki/Documentation#PERFORMANCE


Example
-------

>>> from libleipzig import * # might take some time initially
>>> r = list(Baseform("Schlangen"))
>>> r
[(Grundform: Schlange, Wortart: N), (Grundform: Schlangen, Wortart: S)]
>>> r[0].Grundform
u'Schlange'
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
