import numpy as np
import pickle
import sys
import os
import settings


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


if __name__ == '__main__':
    name = sys.argv[1]
    word = sys.argv[2]
    file = name + '.pkl'
    input_path = os.path.join(settings.MODEL_DIR, file)
    with open(input_path, 'rb') as f:
        model = pickle.load(f)
    sentence = generate(word, model)
    print(sentence)
