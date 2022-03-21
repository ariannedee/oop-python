import random


class Player:
    def __init__(self, num):
        self._score = 0
        self.num = num

    @property
    def score(self):
        return self._score

    def take_turn(self):
        roll = self._roll()
        self._score += roll
        print(f'{self} rolled a {roll} ({self.score})')

    @staticmethod
    def _roll():
        return random.randint(1, 6)

    def __str__(self):
        return f'Player {self.num}'

    def __repr__(self):
        return f'Player({self.num})'
