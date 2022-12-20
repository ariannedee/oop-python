from random import randint, random

class MethodNotDefined(Exception):
    pass


class RollerMixin:
    @staticmethod
    def roll_die():
        raise MethodNotDefined()


class Player(RollerMixin):
    def __init__(self, num):
        self.num = num
        self._score = 0

    def take_turn(self):
        roll = self.roll_die()
        self._score += roll
        print(f"{self}: {self._score} (rolled a {roll})")

    @staticmethod
    def roll_die():
        return randint(1, 6)

    @property
    def score(self):
        return self._score

    def __str__(self):
        return f"Player {self.num}"


class LuckyPlayer(Player):
    @staticmethod
    def roll_die():
        return randint(3, 6)

    def __str__(self):
        base = super().__str__()
        return f"{base} (lucky)"


def get_player(num):
    if random() > 0.5:
        return Player(num)
    return LuckyPlayer(num)
