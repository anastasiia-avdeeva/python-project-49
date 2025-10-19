from brain_games.cli import welcome_user


def main():
    user_name = welcome_user()
    return user_name


if __name__ == 'main':
    main()
