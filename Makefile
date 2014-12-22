
all: build docs_html

build:
	@echo "Building module..."
	python setup.py sdist bdist_wheel

docs_html:
	@echo "Creating html docs..."
	make -C docs/ html

publish:
	@echo "Publishing to PyPI..."
	twine upload dist/*

clean:
	@echo "Cleaning Python builds..."
	python setup.py clean --all

clean_all:
	@echo "Cleaning All Python builds..."
	python setup.py clean --all
	rm -fr dist/
