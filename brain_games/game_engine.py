import prompt

ROUND_NUM = 3


def handle_wrong_answer(
        user_answer: str, right_answer: str, user_name: str) -> None:
    print(f'"{user_answer}" is wrong answer ;(.', end=' ')
    print(f'Correct answer was "{right_answer}".')
    print(f'Let\'s try again, {user_name}!')


def play(user_name: str, game_module) -> None:
    print(game_module.get_rules())

    for _ in range(ROUND_NUM):
        question, answer = game_module.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer != answer:
            handle_wrong_answer(str(user_answer), str(answer), user_name)
            return
        print('Correct!')

    print(f'Congratulations, {user_name}!')
