PYTHON = python

test:
	@nosetests --with-doctest --doctest-extension=rst --detailed-errors

clean:
	find . -name '*.py[co]' -exec rm -f {} ';'

