"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from random import randint


def run_game(num_players=2, target_score=100):
    scores = [0] * num_players

    while True:
        for i, score in enumerate(scores):
            roll = randint(1, 6)
            score += roll
            scores[i] = score
            print(f"Player {i + 1}: {score} (rolled a {roll})")
            if score >= target_score:
                print(f"Player {i + 1} wins!")
                return


if __name__ == '__main__':
    print("---- GAME 1 START ----")
    run_game(num_players=3, target_score=50)
    print("---- GAME 1 END ----")
    print()
    print("---- GAME 2 START ----")
    run_game(num_players=4, target_score=60)
    print("---- GAME 2 END ----")
