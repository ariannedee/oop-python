"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from random import randint


def play_game(num_players=2, target_score=100):
    scores = [0] * num_players

    while True:
        for i, score in enumerate(scores):
            player_num = i + 1
            roll = randint(1, 6)
            score += roll
            scores[i] = score
            print(f"Player {player_num}: {score} (rolled a {roll})")
            if score >= target_score:
                print(f'Player {player_num} wins!')
                return


if __name__ == '__main__':
    print("--- START GAME 1 ---")
    play_game(3, 50)
    print("--- END GAME 1 ---")
    print("--- START GAME 2 ---")
    play_game(4, 60)
    print("--- END GAME 2 ---")
