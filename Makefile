TESTDIR = ./.test
PYTHON = python
VIRTUALENV = virtualenv
PYVER = $(shell $(PYTHON) -V 2>&1 | grep -o '[0-9].[0-9]')
SOURCES = $(wildcard libleipzig/*.py) $(wildcard tests/*.py) \
          README.rst setup.py
.PHONY: install build dist test clean distclean virtualenv docs

test: virtualenv
	@cd "$(TESTDIR)"; PYTHONPATH= \
	./bin/nosetests --with-doctest --doctest-extension=rst --detailed-errors libleipzig.test ../README.rst

virtualenv: $(TESTDIR) \
	$(TESTDIR)/lib/python$(PYVER)/site-packages/suds \
	$(TESTDIR)/lib/python$(PYVER)/site-packages/libleipzig \
	$(TESTDIR)/bin/nosetests
$(TESTDIR):
	$(VIRTUALENV) --clear --no-site-packages --distribute "$(TESTDIR)"
$(TESTDIR)/lib/python$(PYVER)/site-packages/suds:
	$(TESTDIR)/bin/pip -q install suds
$(TESTDIR)/lib/python$(PYVER)/site-packages/libleipzig: $(SOURCES)
	$(TESTDIR)/bin/python setup.py --quiet install
$(TESTDIR)/bin/nosetests:
	$(TESTDIR)/bin/pip -q install nose

install:
	$(PYTHON) setup.py install

build:
	$(PYTHON) setup.py build

dist: docs
	$(PYTHON) setup.py sdist

docs: manual.html
manual.html: README.rst libleipzig/protocol.py gendocs
	./gendocs | rst2html - manual.html

clean:
	find . -name '*.py[co]' -exec rm -f {} ';'
	rm -rf build/ dist/
	rm -f manual.html
	rm -rf "$(TESTDIR)"

distclean: clean
	rm -rf /tmp/suds/
