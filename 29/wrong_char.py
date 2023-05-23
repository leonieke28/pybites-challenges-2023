def get_index_different_char(chars):
    alphanums = []
    non_alphanums = []
    for i, char in enumerate(chars):
        if str(char).isalnum():
            alphanums.append((i, char))
        else:
            non_alphanums.append((i, char))

    if len(alphanums) > len(non_alphanums):
        return non_alphanums[0][0]
    else:
        return alphanums[0][0]
