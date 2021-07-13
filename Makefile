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
  find tests -type d | xargs nosetests --with-coverage --cover-inclusive --cover-erase --cover-package=twilio; \
  coverage xml --omit 'twilio/rest/*' -o coverage.xml

cover-sonar: test-install
	. venv/bin/activate; \
	coverage run --omit=tests/integration/** -m unittest; \
	coverage xml -o coverage-reports/coverage.xml -i

docs-install:
	. venv/bin/activate; pip install -r tests/requirements.txt

docs:
	-rm -rf docs/source/_rst
	-rm -rf docs/build
	. venv/bin/activate; sphinx-apidoc -f twilio -o docs/source/_rst
	. venv/bin/activate; sphinx-build -b html -c ./docs -d docs/build/doctrees . docs/build/html


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

API_DEFINITIONS_SHA=$(shell git log --oneline | grep Regenerated | head -n1 | cut -d ' ' -f 5)
docker-build:
	docker build -t twilio/twilio-python .
	docker tag twilio/twilio-python twilio/twilio-python:${TRAVIS_TAG}
	docker tag twilio/twilio-python twilio/twilio-python:apidefs-${API_DEFINITIONS_SHA}
	docker tag twilio/twilio-python twilio/twilio-python:latest

docker-push:
	echo "${DOCKER_PASSWORD}" | docker login -u "${DOCKER_USERNAME}" --password-stdin
	docker push twilio/twilio-python:${TRAVIS_TAG}
	docker push twilio/twilio-python:apidefs-${API_DEFINITIONS_SHA}
	docker push twilio/twilio-python:latest
