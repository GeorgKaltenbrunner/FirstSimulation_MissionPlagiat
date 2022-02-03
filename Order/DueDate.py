import random
from datetime import datetime, timedelta


def get_due_date(start, end, format):
    s = datetime.strptime(start, format)
    e = datetime.strptime(end, format)

    delta = e - s

    return s + timedelta(days= (random.random() * delta.days))

print(get_due_date("2021/02/01", "2022/03/01", "%Y/%m/%d"))