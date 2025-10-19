from brain_games.cli import welcome_user
from brain_games.game_even import play_even


def main():
    user_name = welcome_user()
    play_even(user_name)


if __name__ == 'main':
    main()
