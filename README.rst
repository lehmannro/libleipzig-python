``libleipzig`` -- wortschatz.uni-leipzig.de binding
===================================================

**libleipzig-python** provides a wrapper to the web services provided by
`Wortschatz Universität Leipzig`_.

.. _Wortschatz Universität Leipzig: http://wortschatz.uni-leipzig.de/

>>> from libleipzig import *
>>> r = list(Baseform("Schlangen"))
>>> r
[(Grundform: Schlange, Wortart: N), (Grundform: Schlangen, Wortart: S)]
>>> r[0].Grundform
'Schlange'
>>> print Baseform.__doc__.splitlines()
Baseform(Wort) -> Grundform, Wortart
>>>

Dependencies
------------

- suds_ 0.3.7 beta or higher

.. _suds: https://fedorahosted.org/suds/#Resources
