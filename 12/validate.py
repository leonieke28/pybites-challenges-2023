from collections import namedtuple

User = namedtuple("User", "name role expired")
USER, ADMIN = "user", "admin"
SECRET = "I am a very secret token"

julian = User(name="Julian", role=USER, expired=False)
bob = User(name="Bob", role=USER, expired=True)
pybites = User(name="PyBites", role=ADMIN, expired=False)
USERS = (julian, bob, pybites)


class UserDoesNotExist(Exception):
    pass


class UserAccessExpired(Exception):
    pass


class UserNoPermission(Exception):
    pass


def get_secret_token(username):
    for user in USERS:
        if user.name == username:
            if user.expired:
                raise UserAccessExpired(f"{username}'s access has expired.")
            elif user.role != ADMIN:
                raise UserNoPermission(f"{username} does not have the ADMIN role.")
            else:
                return SECRET
    raise UserDoesNotExist(f"{username} does not exist.")
