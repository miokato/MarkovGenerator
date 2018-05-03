Simple text generator using 1 Markov process.

## Install
```
$ brew install mecab mecab-ipadic
$ pip install -r requirements.txt
$ python setup.py install
```


## Getting started

```
$ make train name=asuka
$ python

>>> from MKGen.genarator import generate
>>> import pickle
>>> with open('models/asuka.pkl', 'rb') as f:
>>>     model = pickle.load(f)
>>> sentence = generate('こんにちは', model, num_of_words=30)
>>> print(sentence)
```


