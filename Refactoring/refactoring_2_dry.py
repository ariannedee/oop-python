"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from random import randint


def run_game(num_players=2, target_score=100):
    scores = [0 for _ in range(num_players)]

    while True:
        for i, score in enumerate(scores):
            player_num = i + 1
            roll = randint(1, 6)
            score += roll
            scores[i] = score
            print(f"Player {player_num}: {score} (rolled a {roll})")
            if score >= target_score:
                print(f"Player {player_num} wins!")
                return


if __name__ == '__main__':
    print("---- GAME 1 START ----")
    run_game(num_players=4, target_score=20)
    print("---- GAME 1 END ----")
    print()
    print("---- GAME 2 START ----")
    run_game(num_players=3, target_score=50)
    print("---- GAME 2 END ----")
