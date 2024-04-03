"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from random import randint


class Player:
    def __init__(self, num):
        self.score = 0
        self.num = num

    def take_turn(self):
        roll = randint(1, 6)
        self.score += roll
        print(f"{self}: {self.score} (rolled a {roll})")

    def __str__(self):
        return f"Player {self.num}"

    def __repr__(self):
        return f"{type(self).__name__}({self.num}, score={self.score})"


def run_game(num_players=2, target_score=100):
    players = [Player(i + 1) for i in range(num_players)]

    while True:
        for player in players:
            player.take_turn()
            if player.score >= 100:
                print(f"{player} wins!")
                return


if __name__ == '__main__':
    print("--- GAME 1 START ---")
    run_game(num_players=5, target_score=30)
    print("--- GAME 1 END ---")
    print()
    print("--- GAME 2 START ---")
    run_game(num_players=3, target_score=60)
    print("--- GAME 2 END ---")
