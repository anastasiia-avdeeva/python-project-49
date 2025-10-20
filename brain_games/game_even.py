from random import randint

import prompt


def is_even(num: int) -> bool:
    return num % 2 == 0


def get_user_answer():
    answer = prompt.string('Your answer: ', empty=True)
    return answer or ''


def handle_wrong_answer(
        user_answer: str | int, right_answer: str | int, user_name: str):
    print(f'"{user_answer}" is wrong answer ;(.', end=' ')
    print(f'Correct answer was "{right_answer}".')
    print(f'Let\'s try again, {user_name}!')


def play_even(user_name: str):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(3):
        # Non-security use of random is safe in this context
        # noinspection S2245
        num = randint(1, 100)
        print(f'Question: {num}')
        user_answer = get_user_answer()
        right_answer = 'yes' if is_even(num) else 'no'
        if user_answer != right_answer:
            handle_wrong_answer(user_answer, right_answer, user_name)
            return
        print('Correct!')

    print(f'Congratulations, {user_name}!')
