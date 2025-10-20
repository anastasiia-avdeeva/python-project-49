import prompt

from brain_games.games.calc import get_expression, solve_expression
from brain_games.games.even import get_random_int, is_even


def print_intro(game):
    match game:
        case 'even':
            print('Answer "yes" if the number is even, otherwise answer "no".')
            return
        case 'calc':
            print('What is the result of the expression?')


def get_question(game: str) -> int | str | None:
    match game:
        case 'even':
            return get_random_int()
        case 'calc':
            return get_expression()


def ask_question(question: str) -> None:
    print(f'Question: {question}')


def get_right_answer(game: str, question: str) -> str | int | None:
    match game:
        case 'even':
            return 'yes' if is_even(int(question)) else 'no'
        case 'calc':
            return solve_expression(question)


def get_user_answer(game: str) -> str | int | None:
    answer = ''
    message = 'Your answer: '
    match game:
        case 'even':
            answer = prompt.string(message)
        case 'calc':
            answer = prompt.integer(message)
    return answer


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
