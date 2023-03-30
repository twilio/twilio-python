.PHONY: clean install analysis test test-install test-docker develop docs docs-install prettier prettier-check

venv:
	@python --version || (echo "Python is not installed, Python 3.7+"; exit 1);
	virtualenv --python=python venv

install: venv
	. venv/bin/activate; pip install .

test-install: install
	. venv/bin/activate; pip install -r tests/requirements.txt

test-docker:
	docker build -t twilio/twilio-python .
	docker run twilio/twilio-python pytest tests --ignore=tests/cluster

develop: venv
	. venv/bin/activate; pip install -e . --use-mirrors
	. venv/bin/activate; pip install -r tests/requirements.txt

analysis:
	. venv/bin/activate; flake8 --ignore=E123,E126,E128,E501,W391,W291,W293,F401,W503,E203 tests
	. venv/bin/activate; flake8 --ignore=E402,F401,W391,W291,W293,W503,E203 twilio --max-line-length=300

test: analysis prettier-check
	. venv/bin/activate; pytest tests --ignore=tests/cluster

test-with-coverage: prettier-check
	. venv/bin/activate; \
  	pytest --cov-config=setup.cfg --cov-report xml --cov=twilio tests --ignore=tests/cluster

cluster-test:
	. venv/bin/activate; pytest tests/cluster

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

prettier:
	. venv/bin/activate; autoflake --remove-all-unused-imports -i -r --exclude venv .
	. venv/bin/activate; black .

prettier-check:
	. venv/bin/activate; autoflake --check-diff --quiet --remove-all-unused-imports -r --exclude venv .
	. venv/bin/activate; black --check .

API_DEFINITIONS_SHA=$(shell git log --oneline | grep Regenerated | head -n1 | cut -d ' ' -f 5)
CURRENT_TAG=$(shell expr "${GITHUB_TAG}" : ".*-rc.*" >/dev/null && echo "rc" || echo "latest")
docker-build:
	docker build -t twilio/twilio-python .
	docker tag twilio/twilio-python twilio/twilio-python:${GITHUB_TAG}
	docker tag twilio/twilio-python twilio/twilio-python:apidefs-${API_DEFINITIONS_SHA}
	docker tag twilio/twilio-python twilio/twilio-python:${CURRENT_TAG}

docker-push:
	docker push twilio/twilio-python:${GITHUB_TAG}
	docker push twilio/twilio-python:apidefs-${API_DEFINITIONS_SHA}
	docker push twilio/twilio-python:${CURRENT_TAG}
