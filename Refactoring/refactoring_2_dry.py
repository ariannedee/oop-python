"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from random import randint


def play_game():
    player_scores = [0, 0]
    while True:
        for i, score in enumerate(player_scores):
            roll = randint(1, 6)
            score += roll
            player_scores[i] = score
            player_num = i + 1
            print(f"Player {player_num}: {score} (rolled a {roll})")
            if score >= 100:
                print(f"Player {player_num} wins")
                return


if __name__ == '__main__':
    play_game()
