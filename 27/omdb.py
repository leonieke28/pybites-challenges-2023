import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies = []
    for file in files:
        with open(file) as f:
            movie_json = json.load(f)
            movies.append(movie_json)
    return movies


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if "Comedy" in movie["Genre"]:
            return movie["Title"]


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    most_nominations = 0
    movie_with_most_nominations = ""
    for movie in movies:
        if "Awards" in movie:
            nominations = int(movie["Awards"].split("&")[1].strip().split()[0])
            if nominations > most_nominations:
                most_nominations = nominations
                movie_with_most_nominations = movie["Title"]
    return movie_with_most_nominations


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    longest_runtime = 0
    movie_with_longest_runtime = ""
    for movie in movies:
        if "Runtime" in movie:
            runtime = int(movie["Runtime"].split()[0])
            if runtime > longest_runtime:
                longest_runtime = runtime
                movie_with_longest_runtime = movie["Title"]
    return movie_with_longest_runtime
