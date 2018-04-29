.PHONY: test
test:
	echo ${name}


.PHONY: train
train:
	python train.py ${name}
	@echo 'Done! created ${name}.pkl'


.PHONY: gen
gen:
	python generator.py ${name} ${word}


