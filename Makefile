SHELL:=/bin/bash -O extglob
DOCS_FILES = $(shell find docs -type f -not -path 'docs/_build/*' -not -path '**/.DS_Store')
TESTS_FILES = $(shell find tests -type f -name '*_test.py')
MODULE_FILES = $(shell find bibscrap -type f -not -path '**/.DS_Store')

bold := $(shell tput bold)
sgr0 := $(shell tput sgr0)

.PHONY:
help:  ## show this help
	@echo "$(bold)bibscrap Makefile$(sgr0)"
	@echo "Please use 'make target' where target is one of:"
	@cat $(MAKEFILE_LIST) \
		| grep -ve '^#' -ve 'sed.*##' \
		| sed -ne '/@cat/!s/## /## /p' \
		| sed -e 's/: .*##/ ##/g' \
		| column -t -s'##' \
        | sed -e 's/^/  /g'

.PHONY: test
test:
	pipenv run python -m tox
	pipenv run coverage report -m

build: ## Build distribution.
	pipenv run python -m build --wheel --sdist
	pipenv run twine check dist/*

.PHONY: docs
docs: docs/_build/html  ## generate documentation

docs/_build/html: $(DOCS_FILES) $(MODULE_FILES) docs/requirements.txt
	cd docs; pipenv run make clean html

docs/requirements.txt: Pipfile.lock
	pipenv run pip freeze > docs/requirements.txt

Pipfile.lock:
	pipenv lock --pre

.PHONY: testupload
testupload: build  ## upload distribution to test.pypi.org
	pipenv run twine check dist/*
	pipenv run twine upload --repository testpypi dist/*

.PHONY: upload
upload: build  ## upload distribution to pypi.org
	pipenv run twine check dist/*
	pipenv run twine upload dist/*

.PHONY: conduct
conduct:
	wget -nv -O CODE_OF_CONDUCT.md \
		https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md
	sed -i '' "s/\[INSERT CONTACT METHOD\]/bibscrap\.dev@gmail\.com/g" CODE_OF_CONDUCT.md

.PHONY: clean
clean:  ## clean build environment
	pipenv run python -c "from setuptools import setup; setup()" clean --all
	rm -f pytest.log
	rm -rf bibscrap.egg-info
	rm -rf dist
