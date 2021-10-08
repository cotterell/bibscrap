.PHONY: build
build:
	pipenv run python -m build --wheel --sdist
	pipenv run twine check dist/*

.PHONY: doc
doc:
	pipenv run pip freeze > docs/requirements.txt
	cd docs; pipenv run make clean html

.PHONY: testupload
testupload: build
	pipenv run twine check dist/*
	pipenv run twine upload --repository testpypi dist/*

.PHONY: upload
upload: build
	pipenv run twine check dist/*
	pipenv run twine upload dist/*

.PHONY: conduct
conduct:
	wget -nv -O CODE_OF_CONDUCT.md \
		https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md
	sed -i '' "s/\[INSERT CONTACT METHOD\]/bibscrap\.dev@gmail\.com/g" CODE_OF_CONDUCT.md
	pandoc CODE_OF_CONDUCT.md -f markdown -t rst -o CODE_OF_CONDUCT.rst

.PHONY: clean
clean:
	pipenv run python -c "from setuptools import setup; setup()" clean --all
	rm -f CODE_OF_CONDUCT.md
	rm -rf bibscrap.egg-info
	rm -rf dist
