"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
import random


def play_game():
    scores = [0, 0]

    while True:
        for i, score in enumerate(scores):
            player_num = i + 1
            roll = random.randint(1, 6)
            score += roll
            scores[i] = score
            print(f"Player {player_num} score: {score} (rolled a {roll})")
            if score >= 100:
                print(f"Player {player_num} wins!")
                return


if __name__ == '__main__':
    play_game()
