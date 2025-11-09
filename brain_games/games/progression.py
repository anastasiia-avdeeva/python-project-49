from random import randint


def make_progression() -> list[str]:
    start = randint(-10, 50)
    step = randint(-10, 10)
    while step == 0:
        step = randint(-10, 10)
    length = randint(5, 10)
    return [str(start + i * step) for i in range(length)]


def hide_num_in_progresion(progression: list) -> tuple[str, str]:
    length = len(progression)
    rand_i = randint(0, length - 1)
    hidden_num = progression[rand_i]
    result = progression[0:rand_i] + ['..'] + progression[rand_i + 1:length]
    return (" ".join(result), hidden_num)


def get_rules() -> str:
    return 'What number is missing in the progression?'


def get_question_and_answer() -> tuple[str, str]:
    progression = make_progression()
    return hide_num_in_progresion(progression)
