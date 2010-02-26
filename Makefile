PYTHON = python
TESTDIR = ./.test
.PHONY: install build dist test clean distclean virtualenv

install:
	$(PYTHON) setup.py install

build:
	$(PYTHON) setup.py build

dist:
	$(PYTHON) setup.py sdist

test: $(TESTDIR)/bin/nosetests
	@$(TESTDIR)/bin/nosetests --with-doctest --doctest-extension=rst --detailed-errors

virtualenv: $(TESTDIR)
$(TESTDIR):
	@echo "Setting up virtual environment.."
	virtualenv --clear --no-site-packages --distribute "$(TESTDIR)"
	@echo "Installing dependencies.."
	$(TESTDIR)/bin/pip install -U suds
	@echo "Installing libleipzig-python.."
	$(TESTDIR)/bin/python setup.py install
$(TESTDIR)/bin/nosetests: $(TESTDIR)
	$(TESTDIR)/bin/pip install -U nose

docs: libleipzig/protocol.py README.rst
	./gendocs | rst2html - manual.html

clean:
	find . -name '*.py[co]' -exec rm -f {} ';'
	rm -rf build/ dist/
	rm -f MANIFEST manual.html
	rm -rf .test/

distclean: clean
	rm -rf /tmp/suds/
