from pytz import timezone, utc

AUSTRALIA = timezone("Australia/Sydney")
SPAIN = timezone("Europe/Madrid")


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
    tuple of Australian and Spanish (timezone aware) datetimes"""
    utc_dt = naive_utc_dt.replace(tzinfo=utc)
    australian_dt = AUSTRALIA.normalize(utc_dt.astimezone(AUSTRALIA))
    spanish_dt = SPAIN.normalize(utc_dt.astimezone(SPAIN))
    return australian_dt, spanish_dt
