venv:
	virtualenv venv

install: venv
	. venv/bin/activate; pip install .

analysis:
	. venv/bin/activate; flake8 --ignore=E123,E126,E128,E501 tests
	. venv/bin/activate; flake8 --ignore=F401 twilio

test: analysis
	. venv/bin/activate; nosetests
