.PHONY: train
train:
	python main.py ${name}
	@echo 'Done! created ${name}.pkl'


.PHONY: build
build:
	python setup.py sdist


.PHONY: test-upload
test-upload:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*


.PHONY: upload
upload:
	twine upload dist/*



