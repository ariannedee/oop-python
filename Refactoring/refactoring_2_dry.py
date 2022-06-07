"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from random import randint


def play_game(num_players=2):
    scores = [0 for _ in range(num_players)]

    while True:
        for i, score in enumerate(scores):
            player_num = i + 1
            roll = randint(1, 6)
            score += roll
            scores[i] = score
            print(f'Player {player_num} rolled a {roll} ({score})')

            if score >= 100:
                print(f'Player {player_num} wins!')
                return


if __name__ == '__main__':
    print("-- Game 1 start --")
    play_game(num_players=3)
    print("-- Game 1 end --")
    print("-- Game 2 start --")
    play_game(num_players=4)
    print("-- Game 2 end --")
