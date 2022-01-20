"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from random import randint


def run_game():
    player_1_score = 0
    player_2_score = 0

    while True:
        player_1_roll = randint(1, 6)
        player_1_score += player_1_roll
        print(f"Player 1 score: {player_1_score} (rolled a {player_1_roll})")

        if player_1_score >= 100:
            print("Player 1 wins!")
            return

        player_2_roll = randint(1, 6)
        player_2_score += player_2_roll
        print(f"Player 2 score: {player_2_score} (rolled a {player_2_roll})")

        if player_2_score >= 100:
            print("Player 2 wins!")
            return


if __name__ == '__main__':
    print("------ GAME 1 --------")
    run_game()
    print("------ GAME 2 --------")
    run_game()
