def get_users(passwd: str) -> dict:
    """Split password output by newline,
    extract user and name (1st and 5th columns),
    strip trailing commas from name,
    replace multiple commas in name with a single space
    return dict of keys = user, values = name.
    """
    users_dict = {}
    lines = passwd.strip().split("\n")
    for line in lines:
        user_info = line.split(":")
        username = user_info[0]
        name = user_info[4]
        name = name.replace(",,,", "")
        name = name.replace(",", " ")
        if name == "":
            name = "unknown"
        users_dict[username] = name

    return users_dict
