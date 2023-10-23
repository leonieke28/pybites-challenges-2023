import functools

known_users = ["bob", "julian", "mike", "carmen", "sue"]
loggedin_users = ["mike", "sue"]


def login_required(func):
    @functools.wraps(func)
    def wrapper_login_required(user):
        if user not in known_users:
            return func("please create an account")
        elif user in known_users and user not in loggedin_users:
            return func("please login")
        elif user in known_users and user in loggedin_users:
            return func(f"welcome back {user}")

    return wrapper_login_required


@login_required
def welcome(user):
    """Return a welcome message if logged in"""
    return user
