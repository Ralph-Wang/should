TESTS=`find tests -name test_*.py`

test:
	@nosetests $(TESTS)

cov:
	@nosetests --with-coverage --cover-package=should $(TESTS)
	@coverage html

.PHONY: test cov
