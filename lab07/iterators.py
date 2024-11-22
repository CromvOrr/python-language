# 7.6
import itertools
import random


def zero_one_cycle():
    return itertools.cycle([0, 1])


def nesw_random():
    while True:
        yield random.choice(["N", "E", "S", "W"])


def zero_to_six_cycle():
    return itertools.cycle(range(7))
