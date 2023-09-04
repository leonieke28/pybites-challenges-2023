from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if not lst_of_lst:
        return None

    return [lst for sublist in lst_of_lst for lst in sublist + [sep]][:-1]
