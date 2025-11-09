from random import randint


def get_two_random_nums() -> tuple:
    base = randint(2, 10)
    multiplier = randint(1, 10)
    return base * multiplier, base * randint(1, 10)


def calculate_gcd(first_num: int, second_num: int) -> int:
    while second_num != 0:
        first_num, second_num = second_num, first_num % second_num

    return first_num


def get_rules() -> str:
    return 'Find the greatest common divisor of given numbers.'


def get_question_and_answer() -> tuple[str, str]:
    (first_num, second_num) = get_two_random_nums()
    question = f'{first_num} {second_num}'
    answer = calculate_gcd(first_num, second_num)
    return question, str(answer)
