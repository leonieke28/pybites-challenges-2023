import calendar


def weekday_of_birth_date(dt):
    """Takes a date object and returns the corresponding weekday string"""
    return calendar.day_name[dt.weekday()]
