from brain_games.cli import welcome_user
from brain_games.game_engine import play
from brain_games.games import even


def main():
    user_name = welcome_user()
    play(user_name, even)


if __name__ == '__main__':
    main()
