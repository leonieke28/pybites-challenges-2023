from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple("Game", "title link")


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    d = feedparser.parse(FEED_URL)
    titles = [feed["title"] for feed in d["entries"]]
    links = [feed["link"] for feed in d["entries"]]
    return tuple(map(Game, titles, links))


get_games()
