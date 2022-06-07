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
        return f'{type(self).__name__}({self.num})'


class LuckyPlayer(Player):
    @staticmethod
    def _roll_die():
        return randint(3, 6)

    def __str__(self):
        string = super().__str__()
        return f'{string} (lucky)'


def get_player(num):
    if num % 3 == 0:
        return LuckyPlayer(num)
    return Player(num)
