from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    start = PYBITES_BORN + timedelta(days=100)
    while True:
        yield start
        start += timedelta(days=100)


gen_special_pybites_dates()
