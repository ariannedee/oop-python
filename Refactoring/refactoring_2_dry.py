"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from random import randint

game = 0


def run_game(num_players, target_score=100):
    global game
    game += 1
    scores = [0 for _ in range(num_players)]
    print(f"----- GAME {game} START -----")

    while True:
        for i, score in enumerate(scores):
            player_num = i + 1
            roll = randint(1, 6)
            score += roll
            scores[i] = score
            print(f"Player {player_num}: {score} (rolled a {roll})")
            if score >= target_score:
                print(f"Player {player_num} wins!")
                print(f"----- GAME {game} END -----")
                return


if __name__ == '__main__':
    run_game(3, 50)
    run_game(4, 60)
