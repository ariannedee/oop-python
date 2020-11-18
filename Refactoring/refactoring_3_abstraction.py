"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
import random


class Player:
    def __init__(self, player_num):
        self.player_num = player_num
        self._score = 0

    @staticmethod
    def roll_die():
        return random.randint(1, 6)

    def take_turn(self):
        roll = self.roll_die()
        self._score += roll
        print(f"{self} score: {self._score} (rolled a {roll})")

    def has_won(self):
        return self._score >= 100

    @property
    def score(self):
        return self._score

    def __str__(self):
        return f"Player {self.player_num}"


def play_game(num_players):
    players = []
    for i in range(num_players):
        players.append(Player(i + 1))
    while True:
        for player in players:
            player.take_turn()
            if player.has_won():
                print(f"{player} wins!")
                return


if __name__ == '__main__':
    play_game(3)
