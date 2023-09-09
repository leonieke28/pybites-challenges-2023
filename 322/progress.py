from datetime import datetime


def ontrack_reading(books_goal: int, books_read: int, day_of_year: int = None) -> bool:
    if day_of_year is None:
        day_of_year = datetime.now().timetuple().tm_yday

    days_past = (day_of_year / 365) * 100

    should_be_read = (books_goal * days_past) / 100

    if books_read >= should_be_read:
        return True
    else:
        return False
