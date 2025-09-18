"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 50 wins.
"""
from random import randint

def play_game(num_players=2, target_score=50):
    scores = [0 for i in range(num_players)]

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
    print("------ GAME 1 START ------")
    play_game(3, 40)
    print("------ GAME 1 END ------")
    print("------ GAME 2 START ------")
    play_game(4, 30)
    print("------ GAME 2 END ------")
