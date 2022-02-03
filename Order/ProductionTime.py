import random


def production_time(start, end):
    time = random.randint(start, end)
    return time


print(production_time(1, 100))
