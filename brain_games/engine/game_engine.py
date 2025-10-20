from random import randint

import prompt

from brain_games.games.calc import get_expression, solve_expression
from brain_games.games.even import is_even
from brain_games.games.gcd import calculate_gcd, get_two_random_nums
from brain_games.games.prime import is_prime
from brain_games.games.progression import (
    hide_num_in_progresion,
    make_progression,
)


def print_intro(game):
    match game:
        case 'even':
            print('Answer "yes" if the number is even, otherwise answer "no".')
        case 'calc':
            print('What is the result of the expression?')
        case 'gcd':
            print('Find the greatest common divisor of given numbers.')
        case 'progression':
            print('What number is missing in the progression?')
        case 'prime':
            print('Answer "yes" if given number is prime.', end=' ')
            print('Otherwise answer "no".')


def get_question_and_answer(game: str) -> tuple:
    question = ''
    answer = 0
    match game:
        case 'even':
            question = randint(1, 100)
            answer = 'yes' if is_even(question) else 'no'
        case 'calc':
            [operand_1, operator_sign, operand_2] = get_expression()
            question = f'{operand_1} {operator_sign} {operand_2}'
            answer = solve_expression(operand_1, operator_sign, operand_2)
        case 'gcd':
            (first_num, second_num) = get_two_random_nums()
            question = f'{first_num} {second_num}'
            answer = calculate_gcd(first_num, second_num)
        case 'progression':
            progression = make_progression()
            [question, answer] = hide_num_in_progresion(progression)
        case 'prime':
            question = randint(2, 151)
            answer = 'yes' if is_prime(question) else 'no'

    return (question, answer)


def ask_question(question: str) -> None:
    print(f'Question: {question}')


def get_user_answer(game: str) -> str | int | None:
    message = 'Your answer: '
    match game:
        case 'even' | 'prime':
            return prompt.string(message)
        case _:
            return prompt.integer(message)


def handle_wrong_answer(
        user_answer: str, right_answer: str, user_name: str) -> None:
    print(f'"{user_answer}" is wrong answer ;(.', end=' ')
    print(f'Correct answer was "{right_answer}".')
    print(f'Let\'s try again, {user_name}!')


def play(user_name: str, game: str) -> None:
    print_intro(game)

    for i in range(3):
        [question, right_answer] = get_question_and_answer(game)
        ask_question(str(question))
        user_answer = get_user_answer(game)
        if user_answer != right_answer:
            handle_wrong_answer(str(user_answer), str(right_answer), user_name)
            return
        print('Correct!')
    print(f'Congratulations, {user_name}!')
