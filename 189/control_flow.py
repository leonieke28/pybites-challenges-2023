IGNORE_CHAR = "b"
QUIT_CHAR = "q"
MAX_NAMES = 5


def filter_names(names):
    result = []
    for name in names:
        if name.startswith(IGNORE_CHAR):
            continue
        elif any(char.isdigit() for char in name):
            continue
        elif name.startswith(QUIT_CHAR):
            break
        else:
            result.append(name)

    return result[:MAX_NAMES]
