Simple text generator using 1 Markov process.

## Install
```
$ make all
```

## Dependency
- mecab
- mecab-ipadic
- mecab-python3
- numpy
- mecab-ipadic-neologd


## Getting started

```
$ mkdir data
# Creating txt file
$ touch data/asuka.txt
$ make train name=asuka
$ python

>>> from MKGen.genarator import generate
>>> import pickle
>>> with open('models/asuka.pkl', 'rb') as f:
>>>     model = pickle.load(f)
>>> sentence = generate('こんにちは', model, num_of_words=30)
>>> print(sentence)
```


