import pickle

from utils import load_message, Parser
from corpus import create_corpus


def train():
    output = 'models/sample_model.pkl'
    parser = Parser()
    path = 'data/freeza.txt'
    lines = load_message(path)
    model = {}

    for line in lines:
        line = parser.clean(line)
        words = parser.parse(line)
        model.update(create_corpus(words, model))
    with open(output, 'wb') as f:
        pickle.dump(model, f)


