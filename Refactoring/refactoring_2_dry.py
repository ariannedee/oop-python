"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from random import randint


def run_game(num_players=2):
    # scores = []
    # for _ in range(num_players):
    #     scores.append(0)

    scores = [0 for _ in range(num_players)]  # as list comprehension

    print("------ START GAME -------")
    while True:
        for i, score in enumerate(scores):
            player_num = i + 1
            roll = randint(1, 6)
            score += roll
            scores[i] = score
            print(f'Player {player_num} rolled a {roll} ({score})')

            if score >= 100:
                print(f'Player {player_num} wins!')
                print("------ END GAME -------")
                return


if __name__ == '__main__':
    run_game(2)
    run_game(3)
