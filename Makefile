VENV_NAME?=venv
SYSTEM_PYTHON=/usr/bin/env python3.6
PYTHON=${VENV_NAME}/bin/python3

.DEFAULT: help

help:
	@echo "make run"
	@echo "	   run project"
	@echo "make test"
	@echo "	   run all tests"
	@echo "make doc"
	@echo "	   build sphinx documentation"
	@echo "make clean-doc"
	@echo "	   clean sphinx documentation"
	@echo "make install"
	@echo "	   create virtualenv and install requirements"
	@echo "make ipython"
	@echo "	   run ipython inside virtualenv"
	@echo "make clean"
	@echo "	   clean generated files"

run: ensure-venv
	@${PYTHON} src/app.py

ensure-venv:
	@test -d ${VENV_NAME} || (echo "virtualenv not found. '${VENV_NAME}' doesn't exists"; exit 1)

install:
	@echo "Creating virtualenv: ${VENV_NAME}"
	${SYSTEM_PYTHON} -m virtualenv ${VENV_NAME} || (echo "Creating virtualenv failed"; exit 1)
	${VENV_NAME}/bin/pip install -r requirements.txt || (echo "Installing requirements.txt failed"; exit 1)

doc: ensure-venv
	. ${VENV_NAME}/bin/activate && (cd docs; make html)

clean-doc:
	. ${VENV_NAME}/bin/activate && (cd docs; make clean)

test: ensure-venv
	${PYTHON} -m pytest -vvv -s --log-level=DEBUG

clean:
	@echo "--> Cleaning pyc files"
	find . -name "*.pyc" -delete
	rm -rf __pycache__
	@echo "--> Removing virtualenv"
	rm -rf ${VENV_NAME}

ipython: ensure-venv
	@command -v ${VENV_NAME}/bin/ipython3 >/dev/null 2>&1 || ${VENV_NAME}/bin/pip install ipython
	@export PYTHONPATH=src:$${PYTHONPATH} && \
	${VENV_NAME}/bin/ipython

.PHONY: help run ensure-venv install doc clean-doc test clean ipython
