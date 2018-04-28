def create_corpus(sent, current_next):
    """
    :param (list) sent:
    :return (dict) current_text:
    """
    for i, word in enumerate(sent):
        maxlen = len(sent)
        if i+1 < maxlen:
            this_word = sent[i]
            next_word = sent[i + 1]
            if i == 0:
                current_next['START'] = {}
                current_next['START'][this_word] = 1
            if this_word not in current_next.keys():
                current_next[this_word] = {}

            if next_word not in current_next[this_word].keys():
                current_next[this_word][next_word] = 1
            else:
                current_next[this_word][next_word] += 1
    return current_next


