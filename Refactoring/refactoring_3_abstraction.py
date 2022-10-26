"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from random import randint


class Player:
    def __init__(self, number):
        self.score = 0
        self.number = number

    def take_turn(self):
        roll = randint(1, 6)
        self.score += roll
        print(f"{self} rolled a {roll} (total: {self.score})")

    def __str__(self):
        return f"Player {self.number}"

    def __repr__(self):
        return f"Player({self.number})"


def run_game(num_players, target_score=100):
    players = [Player(i + 1) for i in range(num_players)]
    print("--- GAME START ---")
    while True:
        for player in players:
            player.take_turn()
            if player.score >= target_score:
                print(f"{player} wins!")
                print("--- GAME END ---\n")
                return


if __name__ == '__main__':
    run_game(2)
    run_game(3, target_score=40)
