PYTHON = python
.PHONY: install build dist test clean distclean

install:
	$(PYTHON) setup.py install

build:
	$(PYTHON) setup.py build

dist:
	$(PYTHON) setup.py sdist

test:
	@nosetests --with-doctest --doctest-extension=rst --detailed-errors

docs: libleipzig/protocol.py README.rst
	./gendocs | rst2html - manual.html

clean:
	find . -name '*.py[co]' -exec rm -f {} ';'
	rm -rf build/ dist/
	rm -f MANIFEST manual.html

distclean: clean
	rm -rf /tmp/suds/
