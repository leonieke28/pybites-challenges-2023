import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
S3 = "https://bites-data.s3.us-east-2.amazonaws.com/"
DICT = "dictionary.txt"
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(f"{S3}{DICT}", DICTIONARY)

print(DICTIONARY)

scrabble_scores = [
    (1, "E A O I N R T L S U"),
    (2, "D G"),
    (3, "B C M P"),
    (4, "F H V W Y"),
    (5, "K"),
    (8, "J X"),
    (10, "Q Z"),
]
LETTER_SCORES = {
    letter: score for score, letters in scrabble_scores for letter in letters.split()
}

# print(LETTER_SCORES)

# start coding


def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY, mode="r", encoding="utf-8") as file:
        words = [word.rstrip() for word in file]

    # print(words)
    return words


load_words()


def calc_word_value(word):
    """Given a word, calculate its value using the LETTER_SCORES dict"""
    return sum(
        LETTER_SCORES[letter] if letter in LETTER_SCORES else 0
        for letter in word.upper()
    )


def max_word_value(words):
    """Given a list of words, calculate the word with the maximum value and return it"""
    max_value = 0
    max_word = ""
    for word in words:
        value = calc_word_value(word)
        if value > max_value:
            max_value = value
            max_word = word
    return max_word
