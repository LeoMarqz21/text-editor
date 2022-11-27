from datetime import datetime


def displayDate():
    date = datetime.now()
    return 'Date: {}/{}/{}'.format(date.day, date.month, date.year)

