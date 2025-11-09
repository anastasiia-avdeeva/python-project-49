from random import randint


def is_prime(num) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_rules() -> str:
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer() -> tuple[str, str]:
    question = randint(2, 151)
    answer = 'yes' if is_prime(question) else 'no'
    return str(question), answer
