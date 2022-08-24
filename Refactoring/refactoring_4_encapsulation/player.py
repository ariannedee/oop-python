from random import randint


class Player:
    def __init__(self, player_num):
        self.num = player_num
        self._score = 0

    def take_turn(self):
        roll = randint(1, 6)
        self._score += roll
        print(f'{self} rolled a {roll} ({self._score})')

    @property
    def score(self):
        return self._score

    def __str__(self):
        return f'Player {self.num}'

    def __repr__(self):
        return f'Player({self.num})'
