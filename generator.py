import numpy as np
import pickle


def generate(word, dic, num_of_words=30):
    """
    :param (str) word:
    :param (dict) dic:
    :param (int) num_of_words:
    :return (str) result:
    """
    if word not in dic.keys():
        all_words = list(dic.keys())
        next_word = np.random.choice(all_words)
    else:
        next_word = word
    sent = []
    sent.append(next_word)
    for i in range(num_of_words):
        word_probas = dic[next_word]
        next_words, weight = [], []
        for w, wt in word_probas.items():
            next_words.append(w)
            weight.append(wt)
        weight = [w/sum(weight) for w in weight]
        expected = np.random.choice(next_words, p=weight)
        sent.append(expected)
        next_word = expected
    result = ''.join(sent)
    return result


def main():
    path = 'models/sample_model.pkl'
    with open(path, 'rb') as f:
        model = pickle.load(f)
    sentence = generate('私', model)
    print(sentence)
