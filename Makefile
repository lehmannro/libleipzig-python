PYTHON = python
.PHONY: install build dist test clean distclean docs

test:
	$(PYTHON) setup.py --quiet test --verbose

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
	rm -rf build/ dist/ libleipzig.egg-info/
	rm -rf suds-*.egg/ nose-*.egg/
	rm -f MANIFEST manual.html

distclean: clean
	rm -rf /tmp/suds/
