def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
    (1995, 19ab = numbers / Happy, happy4you = strings, hence for
     numbers you only need to check the first char of the word)
    """
    words_starting_with_letter = []
    words_starting_with_number = []

    for word in words:
        if word[0].isdigit():
            words_starting_with_number.append(word)
        else:
            words_starting_with_letter.append(word)

    words_starting_with_letter.sort(key=str.lower)
    words_starting_with_number.sort(key=str.lower)

    return words_starting_with_letter + words_starting_with_number
