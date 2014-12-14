
test:
	@nosetests test.py

cov:
	@nosetests --with-coverage test.py
	@coverage html

.PHONY: test cov
