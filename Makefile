
test:
	@nosetests test.py

cov:
	@nosetests --with-coverage --cover-package=should.py test.py
	@coverage html

.PHONY: test cov
