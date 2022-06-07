from random import randint


class Player:
    def __init__(self, num):
        self._score = 0
        self.num = num

    def make_move(self):
        roll = self._roll_die()
        self._score += roll
        print(f'{self} rolled a {roll} ({self._score})')

    @property
    def score(self):
        return self._score

    @staticmethod
    def _roll_die():
        return randint(1, 6)

    def __str__(self):
        return f'Player {self.num}'

    def __repr__(self):
        return f'Player({self.num})'
