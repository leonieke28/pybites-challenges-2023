import itertools
from collections import Counter
from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    filtered_args = list(filter(None, args))

    if not filtered_args:
        return set()

    elif len(filtered_args) == 1:
        return set(filtered_args[0])

    else:
        return _get_most_common_elements(filtered_args)


def _get_most_common_elements(filtered_args):
    unique_args = [set(i) for i in filtered_args]

    flattened_list = list(itertools.chain(*unique_args))

    counts = Counter(flattened_list)
    max_count = counts.most_common(1)[0][1]
    result = [value for value, count in counts.most_common() if count == max_count]
    return set(result)
