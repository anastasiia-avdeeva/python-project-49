from random import randint


def is_even(num: int) -> bool:
    return num % 2 == 0


def get_rules() -> str:
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer() -> tuple[str, str]:
    question = randint(1, 100)
    answer = 'yes' if is_even(question) else 'no'
    return str(question), answer
