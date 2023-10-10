import csv
from collections import defaultdict, namedtuple
import os
from pathlib import Path
from statistics import mean
from urllib.request import urlretrieve

TMP = Path(os.getenv("TMP", "/tmp"))
S3 = "https://bites-data.s3.us-east-2.amazonaws.com/"
DATA = "movie_metadata.csv"

DATA_LOCAL = TMP / DATA
if not Path(DATA_LOCAL).exists():
    urlretrieve(S3 + DATA, DATA_LOCAL)

MOVIE_DATA = DATA_LOCAL
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple("Movie", "title year score")


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies_by_director = defaultdict(list)

    with open(MOVIE_DATA, mode="r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            if not row["title_year"]:
                continue

            director = row["director_name"]
            title = row["movie_title"].replace("\xa0", "")
            year = int(row["title_year"])
            score = float(row["imdb_score"])

            if year >= MIN_YEAR and director and title and year and score:
                movies_by_director[director].append(Movie(title, year, score))

    return movies_by_director


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
    round the mean to 1 decimal place"""
    return round(mean(movie.score for movie in movies), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
    return a list of tuples (director, average_score) ordered by highest
    score in descending order. Only take directors into account
    with >= MIN_MOVIES"""
    scores = []
    for director, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            average_score = calc_mean_score(movies)
            scores.append((director, average_score))
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores
