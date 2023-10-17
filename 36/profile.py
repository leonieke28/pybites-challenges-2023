def get_profile(name, age, *sports, **awards):
    if not isinstance(age, int):
        raise ValueError("Age must be an integer.")
    if len(sports) > 5:
        raise ValueError("Only up to 5 sports are allowed.")

    profile = {"name": name, "age": age}

    if sports:
        profile["sports"] = list(sorted(sports))

    if awards:
        profile["awards"] = awards

    return profile
