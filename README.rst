=================================================
 libleipzig -- wortschatz.uni-leipzig.de binding
=================================================

**libleipzig-python** provides a wrapper to the web services provided by the
`Deutscher Wortschatz`_ project of the University of Leipzig.  **Deutscher
Wortschatz** is a German database of text corpora and can be utilized to
analyze and contextualize words in the thesaurus.  *libleipzig* currently
supports all public service calls.  These do not require authentication and are
provided `free of charge`_ for private or scientific purposes (even though you
can supply Level-2 credentials for rate limiting purposes).

.. _Deutscher Wortschatz: http://wortschatz.uni-leipzig.de/
.. _free of charge: http://wortschatz.uni-leipzig.de/use.html

.. contents::

.. attention:: libleipzig prefetches__ *all* service interfaces on initial
   load. This process requires an Internet connection.

   Subsequent ``import``\ s use indefinitely cached definitions (WSDL files).

   __ https://fedorahosted.org/suds/wiki/Documentation#PERFORMANCE


Example
-------

>>> from libleipzig import * # might take some time initially
>>> r = Baseform(u"Schlangen")
>>> r # doctest: +NORMALIZE_WHITESPACE
[(Grundform: u'Schlange', Wortart: u'N'),
 (Grundform: u'Schlangen', Wortart: u'S')]
>>> r[0].Grundform
u'Schlange'
>>> help(Baseform) # doctest: +NORMALIZE_WHITESPACE
Help on function Baseform in module libleipzig.protocol:
Baseform(*vectors, **options)
    Baseform(Wort) -> Grundform, Wortart
        Return the lemmatized (base) form.
>>>

.. **

Dependencies
------------

- Python 2.5 or later 2.x releases
- Setuptools_
- suds_ 0.3.9 or later

.. _Setuptools: http://packages.python.org/distribute/
.. _suds: https://fedorahosted.org/suds/#Resources

Service calls
-------------

Every service calls takes exactly its request parameters (as defined in the
`list of webservices`__) as positional or keyword arguments and accepts a
number of generic options:

auth
  Authentication credentials;  a tuple of (username, password).
  See `Authentication`_.
corpus
  Language corpus;  a string identifier.
  See `Corpora`_.

__ http://wortschatz.uni-leipzig.de/axis/servlet/ServiceOverviewServlet

In case of a remote error all services will throw a `suds.WebFault` (which can
be readily imported from ``libleipzig``).

Corpora
-------

The project collects corpora in a variety of languages, German (*de*) only
being the largest one and thus the default.  According to the reference
implementation the following corpora are available (those marked with asterisks
actually worked as of the time of writing):

* de* (default)
* en*
* es*
* fr*
* fr05*
* fr05_100K
* fr05_1M
* fr05_300K
* fr05_3M*
* it*
* it100K
* it300K
* it10M
* it3M
* nl*
* nl100K
* nl300K
* nl1M

Note that these collections are not as comprehensive as the German corpus and
thus might only provide selected services.  Most often these are the simple
text processing calls such as ``RightNeighbours``.  You can use these corpora
in libleipzig by supplying the ``corpus`` parameter to any of the service
calls:

>>> import libleipzig
>>> libleipzig.Cooccurrences("programming", 0, 1, corpus="en")
[(Wort: u'programming', Kookkurrenz: u'language', Signifikanz: u'4152')]

Authentication
--------------

You can increase your rate limit or gain access to private services by
supplying authentication credentials to a service call::

    Baseform("programming", auth=("username", "password"))

Public service calls can be accessed with the combination anonymous/anonymous,
which is also the default.  If you wish to persist your credentials among
several calls (to the same service) you can save them in the service::

    Baseform.set_credentials("username", "password")
    Baseform("programming")

You should only use the former syntax if you care about thread-safety or do not
want to expose your credentials through the service's transport metadata for
all of the program's runtime.

Troubleshooting
---------------

For unauthenticated service calls the server might raise errors such as the
following::

    suds.WebFault: Server raised fault:
    'java.lang.Exception: Communication link failure,
                          message from server: "Server shutdown in progress"'

This is the API's way to impose rate limits on anonymous users.  See
`Authentication`_ for a way to avoid this issue.

Command-line interface
----------------------

libleipzig provides a commandline tool called ``wortschatz`` which allows a
thin layer upon the programmatic API in an ad-hoc fashion.  It takes the
desired service as its first argument followed by the service's arguments.

The results of the service call are printed in separate lines with the fields
separated by commas (use ``--delimiter`` to modify that behaviour, it
understands patterns such as ``\t`` for TAB).  Use ``--schema`` to obtain the
service's result columns.

You can supply your credentials via ``--user`` and ``--password`` for
authenticated access.

When services are called with the wrong name or wrong number of arguments the
program will terminate with exit code 1.  If the remote server reported failure
(eg. wrong credentials) the program terminates with exit code 2.

Changelog
---------

1.3
  * Added commandline script ``wortschatz`` for ad-hoc access.
  * Jumped to setuptools.
  * Fixed missing return values in services *Sentences* and *Synonyms*.

1.2.1
  * Fixed compatibility issues with suds 0.4.

1.2
  * Added persistable authentication support.
  * Added authentication support.
  * Added different corpora to services.
  * Exposed ``WebFault`` error condition.
  * Extended service parameter by generic options.

1.1
  * Bumped suds version to 0.3.9.
  * Fixed numerous unicode issues and pointed out potential pitfalls.
  * Fixed caching to be persistent but lazy.
  * Upgraded virtual environment to incremental build steps.
  * Pushed tests into installed package.
