"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""


from random import randint

def play_game():
    scores = [0, 0]
    while True:
        for i, _ in enumerate(scores):
            player_number = i + 1
            roll = randint(0, 6)
            scores[i] += roll
            score = scores[i]
            print("player number, score", player_number,scores[i])
            print(f"Player {player_number}: {score} (rolled a {roll})")
            if score >= 100:
                print(f"Player {player_number} wins!")
                print(scores)
                return

if __name__ == '__main__':
    play_game()
