.ve:
	virtualenv .ve

pocket_curator.egg-info: .ve
	./.ve/bin/python setup.py develop

.PHONY: freeze
freeze: .ve
	./.ve/bin/pip install -r requirements-to-freeze.txt
	./.ve/bin/pip freeze > requirements.txt

.PHONY: test
test: .ve pocket_curator.egg-info
	./.ve/bin/py.test tests
