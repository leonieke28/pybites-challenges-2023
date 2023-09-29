import os
import urllib.request
from collections import Counter, namedtuple

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, "dirnames")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/dirnames.txt", tempfile
)

IGNORE = ["static", "templates", "data", "pybites", "bbelderbos", "hobojoe1848"]

Stats = namedtuple("Stats", "user challenge")


def gen_files(tempfile=tempfile):
    """
    Parse the tempfile passed in, filtering out directory names
    (first column) using the last "is_dir" column.

    Lowercase these directory names and return them as a generator.

    The "tempfile" has the following format:
    challenge<int>/file_or_dir<str>,is_dir<bool>

    For example,
    03/rss.xml,False
    03/tags.html,False
    03/Mridubhatnagar,True
    03/aleksandarknezevic,True

    => Here you would return 03/mridubhatnagar (lowercased!)
       followed by 03/aleksandarknezevic
    """
    with open(tempfile) as file:
        content = file.read().splitlines()

    dir_names = []
    for line in content:
        line = line.lower().split(",")
        if line[-1] == "true":
            dir_names.append(line[0])

    return dir_names


def diehard_pybites(files=None):
    """
    Return a Stats namedtuple (defined above) that contains:
    1. The user that made the most pull requests (ignoring the users in IGNORE), and
    2. A tuple of:
        ("most popular challenge id", "the number of pull requests for that challenge")

    Calling this function on the default dirnames.txt should return:

    Stats(user='clamytoe', challenge=('01', 7))
    """
    if files is None:
        files = gen_files()

    challenges = []
    users = []
    for line in files:
        if line.split("/")[1] not in IGNORE:
            challenges.append(line.split("/")[0])
            users.append(line.split("/")[1])

    users = Counter(users).most_common(1)[0][0]
    popular_challenges = Counter(challenges).most_common(1)[0]

    return Stats(users, popular_challenges)
