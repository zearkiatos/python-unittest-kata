run:
	python __main__.py

run-tests:
	 ENVIRONMENT=test python -m unittest discover -s tests -p 'test*.py'