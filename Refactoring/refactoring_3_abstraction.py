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
        self.player_num = player_num

    def take_turn(self):
        roll = self._roll_die()
        self.score += roll
        print(f"{self}: {self.score} (rolled a {roll})")

    @staticmethod
    def _roll_die():
        return randint(1, 6)

    def has_won(self):
        return self.score >= 100

    def __str__(self):
        return f"Player {self.player_num}"

    def __repr__(self):
        return f"Player {self.player_num}: {self.score}"


def play_game(num_players=2):
    players = [Player(i + 1) for i in range(num_players)]  # List comprehension
    while True:
        for player in players:
            player.take_turn()
            if player.has_won():
                print(f"{player} wins")
                return


if __name__ == '__main__':
    play_game(4)
