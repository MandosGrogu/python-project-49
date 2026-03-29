from brain_games.cli import welcome_user
from brain_games.scripts.games.brain_games_list import brain_gcd


def main():

    name = welcome_user()
    brain_gcd(name)


if __name__ == "__main__":

    main()
