"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from random import randint


class Player:
    def __init__(self, player_number):
        self.score = 0
        self.player_number = player_number

    def take_turn(self):
        roll = self._roll_die()
        self.score += roll
        print(f"Player {self.player_number}: {self.score} (rolled a {roll})")

    @staticmethod
    def _roll_die():
        return randint(1, 6)

    @property
    def won_game(self):
        return self.score >= 100

    def __str__(self):
        return f'Player {self.player_number}'


def play_game(num_players=2):
    players = []
    for i in range(num_players):
        players.append(Player(i + 1))
    while True:
        for player in players:
            player.take_turn()
            if player.won_game:
                print(f"{player} wins")
                return


if __name__ == '__main__':
    play_game(4)
