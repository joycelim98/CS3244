def is_hyperlink(word):
    if '/' in word or 'www' in word or '.com' in word or '.gov' in word:
        return 1

    return 0
