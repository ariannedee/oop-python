import random


class Player:
    def __init__(self, player_num):
        self._score = 0
        self._num = player_num

    @staticmethod
    def _roll_die():
        return random.randint(1, 6)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    def take_turn(self):
        roll = self._roll_die()
        self.score += roll
        print(f"{self} rolled a {roll} ({self.score})")

    def __str__(self):
        return f'Player {self._num}'

