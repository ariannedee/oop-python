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
        for i, _ in enumerate(scores):
            player_num = i + 1
            roll = randint(1, 6)
            scores[i] += roll
            score = scores[i]
            print(f"Player {player_num}: {score} (rolled a {roll})")
            if score >= 100:
                print(f"Player {player_num} wins!")
                return


if __name__ == '__main__':
    play_game(3)
