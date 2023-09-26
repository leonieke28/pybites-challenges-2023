def validate_pangram(sentence: str) -> bool:
    """Check if a sentence is a pangram.
    A pangram is a sentence containing every letter in the English alphabet.
    The input `sentence` should be a string containing only English letters.
    The function returns True if the sentence is a pangram, and False otherwise.
    """
    sentence = sentence.replace(" ", "").lower()
    unique_chars = set(sentence)
    return len(unique_chars) == 26
