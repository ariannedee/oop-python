"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from random import randint


class Player:
    def __init__(self, player_num):
        self.score = 0
        self.num = player_num

    @staticmethod
    def _roll():
        return randint(1, 6)

    def make_move(self):
        roll = self._roll()
        self.score += roll
        print(f"{self} score: {self.score} (rolled a {roll})")

    def has_won(self):
        return self.score >= 100

    def __str__(self):
        return f"Player {self.num}"

    def __repr__(self):
        return f"Player({self.num})"


def run_game(num_players=2):
    players = [Player(i + 1) for i in range(num_players)]

    while True:
        for player in players:
            player.make_move()

            if player.has_won():
                print(f"{player} wins!")
                return


if __name__ == '__main__':
    print("------ GAME 1 --------")
    run_game(4)
    print("------ GAME 2 --------")
    run_game(3)
