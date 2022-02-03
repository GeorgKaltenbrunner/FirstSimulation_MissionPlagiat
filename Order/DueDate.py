import random
from datetime import datetime, timedelta


def get_due_date(date_start, date_end, date_format):
    s = datetime.strptime(date_start, date_format)
    e = datetime.strptime(date_end, date_format)

    delta = e - s

    return s + timedelta(days= (random.random() * delta.days))

#print(get_due_date("2021/02/01", "2022/03/01", "%Y/%m/%d"))