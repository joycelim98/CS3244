word_5W1H_list = ["how", "what", "why", "when", "who", "where"]

def starts_with_5W1H(word):
    word = word.lower()
    if word in word_5W1H_list:
        return 1

    return 0

