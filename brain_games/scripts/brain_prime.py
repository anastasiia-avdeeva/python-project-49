from brain_games.cli import welcome_user
from brain_games.game_engine import play
from brain_games.games import prime


def main():
    user_name = welcome_user()
    play(user_name, prime)


if __name__ == '__main__':
    main()
