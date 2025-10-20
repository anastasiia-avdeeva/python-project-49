from random import randint


def is_even(num: int) -> bool:
    return num % 2 == 0


def get_random_int() -> int:
    return randint(1, 100)
