.PHONY: all
all:
	make deps
	make install


.PHONY: deps
deps:
	brew install mecab mecab-ipadic
	git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
	cd mecab-ipadic-neologd && ./bin/install-mecab-ipadic-neologd -n -y
	rm -rf mecab-ipadic-neologd
	pip install -r requirements.txt


.PHONY: install
install:
	python setup.py install


.PHONY: train
train:
	python train.py ${name}
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



