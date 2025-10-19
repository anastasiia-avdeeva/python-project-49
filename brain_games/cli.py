import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string(
        'May I have your name? ').strip().capitalize() or 'stranger'
    print(f'Hello, {name}')
    return name
