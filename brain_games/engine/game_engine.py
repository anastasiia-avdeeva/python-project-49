import prompt

from brain_games.games.calc import get_expression, solve_expression
from brain_games.games.even import get_random_int, is_even
from brain_games.games.gcd import calculate_gcd, get_two_random_nums


def print_intro(game):
    match game:
        case 'even':
            print('Answer "yes" if the number is even, otherwise answer "no".')
        case 'calc':
            print('What is the result of the expression?')
        case 'gcd':
            print('Find the greatest common divisor of given numbers.')


def get_question(game: str) -> int | str | None:
    match game:
        case 'even':
            return get_random_int()
        case 'calc':
            return get_expression()
        case 'gcd':
            (first_num, second_num) = get_two_random_nums()
            return f'{first_num} {second_num}'


def ask_question(question: str) -> None:
    print(f'Question: {question}')


def get_right_answer(game: str, question: str) -> str | int | None:
    match game:
        case 'even':
            return 'yes' if is_even(int(question)) else 'no'
        case 'calc':
            [operand_1, operator_sign, operand_2] = question.split(' ')
            return solve_expression(
                int(operand_1), operator_sign, int(operand_2))
        case 'gcd':
            [first_num, second_num] = question.split(' ')
            return calculate_gcd(int(first_num), int(second_num))


def get_user_answer(game: str) -> str | int | None:
    message = 'Your answer: '
    match game:
        case 'even':
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
        question = get_question(game)
        ask_question(str(question))
        right_answer = get_right_answer(game, str(question))
        user_answer = get_user_answer(game)
        if user_answer != right_answer:
            handle_wrong_answer(str(user_answer), str(right_answer), user_name)
            return
        print('Correct!')
    print(f'Congratulations, {user_name}!')
