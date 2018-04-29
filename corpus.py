def create_corpus(sent, current_next):
    """
    :param (list) sent:
    :return (dict) current_text:
    """
    for i, word in enumerate(sent):
        maxlen = len(sent)
        if i == 0:
            next_word = sent[i + 1]

            if 'START' not in current_next.keys():
                current_next['START'] = {}

            if next_word not in current_next['START'].keys():
                current_next['START'][next_word] = 1
            else:
                current_next['START'][next_word] += 1

        elif i == maxlen - 1:
            this_word = sent[i]

            if this_word not in current_next.keys():
                current_next[this_word] = {}

            if 'END' not in current_next[this_word].keys():
                current_next[this_word]['END'] = 1
            else:
                current_next[this_word]['END'] += 1

        elif i < maxlen - 1:
            this_word = sent[i]
            next_word = sent[i + 1]

            if this_word not in current_next.keys():
                current_next[this_word] = {}

            if next_word not in current_next[this_word].keys():
                current_next[this_word][next_word] = 1
            else:
                current_next[this_word][next_word] += 1

    return current_next


