import numpy as np


def generate(word, model, num_of_words=30):
    """
    :param (str) word:
    :param (dict) model:
    :param (int) num_of_words:
    :return (str) result:
    """
    if word not in model.keys():
        start_words = list(model['START'].keys())
        next_word = np.random.choice(start_words)
    else:
        next_word = word
    sent = []
    sent.append(next_word)
    for i in range(num_of_words):
        if next_word == 'END':
            break
        expected = model[next_word].weighted_random_word()
        sent.append(expected)
        next_word = expected
    result = ''.join(sent)
    result = result.rstrip('END')
    return result
