.PHONY: clean venv install analysis test test-install docs docs-install

venv:
	virtualenv venv

install: venv
	. venv/bin/activate; pip install . --use-mirrors

test-install:
	. venv/bin/activate; pip install -r tests/requirements.txt

analysis:
	. venv/bin/activate; flake8 --ignore=E123,E126,E128,E501 tests
	. venv/bin/activate; flake8 --ignore=F401 twilio

test: analysis
	. venv/bin/activate; nosetests

docs-install:
	. venv/bin/activate; pip install -r docs/requirements.txt

docs:
	. venv/bin/activate; cd docs && make html

clean:
	rm -rf venv
