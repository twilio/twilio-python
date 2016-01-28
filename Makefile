.PHONY: clean venv install analysis test test-install develop docs docs-install

venv:
	virtualenv venv

install: venv
	. venv/bin/activate; pip install . --use-mirrors

test-install: install
	. venv/bin/activate; pip install -r tests/requirements.txt

develop: venv
	. venv/bin/activate; pip install -e . --use-mirrors
	. venv/bin/activate; pip install -r tests/requirements.txt

analysis:
	. venv/bin/activate; flake8 --ignore=E123,E126,E128,E501,W391,W291,W293,F401 tests
	. venv/bin/activate; flake8 --ignore=F401,W391,W291,W293 twilio --max-line-length=300

test: analysis
	. venv/bin/activate; \
  find tests -type d | xargs nosetests

ci:
	flake8 --ignore=E123,E126,E128,E501,W391,W291,W293,F401 tests
	flake8 --ignore=F401,W391,W291,W293 twilio --max-line-length=300
	find tests -type d | xargs nosetests

cover:
	. venv/bin/activate; \
  find tests -type d | xargs nosetests --with-coverage --cover-inclusive --cover-erase --cover-package=twilio

docs-install:
	. venv/bin/activate; pip install -r docs/requirements.txt

docs:
	. venv/bin/activate; cd docs && make html

release: test-install
	. venv/bin/activate; python setup.py sdist upload
	. venv/bin/activate; python setup.py bdist_wheel upload

build: test-install
	. venv/bin/activate; python setup.py sdist
	. venv/bin/activate; python setup.py bdist_wheel

clean:
	rm -rf venv
