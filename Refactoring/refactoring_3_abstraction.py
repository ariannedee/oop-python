"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from random import randint


class Player:
    def __init__(self, num):
        self.num = num
        self.score = 0

    def do_turn(self):
        roll = randint(1, 6)
        self.score += roll
        print(f"{self}: {self.score} (rolled a {roll})")

    def __str__(self):
        return f"Player {self.num}"


def run_game(num_players=2, target_score=100):
    players = [Player(i + 1) for i in range(num_players)]

    while True:
        for player in players:
            player.do_turn()
            if player.score >= target_score:
                print(f"{player} wins!")
                return


if __name__ == '__main__':
    print("---- GAME 1 START ----")
    run_game(num_players=3)
    print("---- GAME 1 END ----")
    print("---- GAME 2 START ----")
    run_game(num_players=2, target_score=40)
    print("---- GAME 2 END ----")
