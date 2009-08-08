PYTHON = python
.PHONY: test clean distclean

test:
	@nosetests --with-doctest --doctest-extension=rst --detailed-errors

docs: README.rst
	@mkdir -p docs
	rst2html README.rst docs/index.html

clean:
	find . -name '*.py[co]' -exec rm -f {} ';'
	rm -rf docs/

distclean: clean
	rm -rf /tmp/suds/
