import datetime


def tomorrow(today=None):
    if today is None:
        return datetime.date.today() + datetime.timedelta(days=1)
    else:
        return today + datetime.timedelta(days=1)
