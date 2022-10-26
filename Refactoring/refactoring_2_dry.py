"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from random import randint


def run_game(num_players, target_score=100):
    scores = [0 for _ in range(num_players)]
    print("--- GAME START ---")
    while True:
        for i, score in enumerate(scores):
            player_num = i + 1
            roll = randint(1, 6)
            score += roll
            scores[i] = score
            print(f"Player {player_num} rolled a {roll} (total: {score})")
            if score >= target_score:
                print(f"Player {player_num} wins!")
                print("--- GAME END ---\n")
                return


if __name__ == '__main__':
    run_game(2)
    run_game(3, target_score=40)
