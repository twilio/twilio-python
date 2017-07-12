.PHONY: clean install analysis test test-install develop docs docs-install

venv:
	@python --version || (echo "Python is not installed, please install Python 2 or Python 3"; exit 1);
	virtualenv --python=python venv

install: venv
	. venv/bin/activate; pip install .

test-install: install
	. venv/bin/activate; pip install -r tests/requirements.txt

develop: venv
	. venv/bin/activate; pip install -e . --use-mirrors
	. venv/bin/activate; pip install -r tests/requirements.txt

analysis:
	. venv/bin/activate; flake8 --ignore=E123,E126,E128,E501,W391,W291,W293,F401 tests
	. venv/bin/activate; flake8 --ignore=E402,F401,W391,W291,W293 twilio --max-line-length=300

test: analysis
	. venv/bin/activate; \
  find tests -type d | xargs nosetests

cover:
	. venv/bin/activate; \
  find tests -type d | xargs nosetests --with-coverage --cover-inclusive --cover-erase --cover-package=twilio

docs-install:
	. venv/bin/activate; pip install pdoc

docs:
	. venv/bin/activate; pdoc twilio --overwrite --html --html-dir docs

release:
	. venv/bin/activate; python setup.py sdist upload
	. venv/bin/activate; python setup.py bdist_wheel upload

build: test-install
	. venv/bin/activate; python setup.py sdist
	. venv/bin/activate; python setup.py bdist_wheel

clean:
	rm -rf venv

nopyc:
	find . -name \*.pyc -delete
