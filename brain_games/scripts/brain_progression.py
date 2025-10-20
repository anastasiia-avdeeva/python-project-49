from brain_games.cli import welcome_user
from brain_games.engine.game_engine import play


def main():
    user_name = welcome_user()
    play(user_name, 'progression')


if __name__ == '__main__':
    main()
