from random import randint


class Player:
    def __init__(self, num):
        self.num = num
        self._score = 0

    @property
    def score(self):
        return self._score

    @staticmethod
    def _roll():
        return randint(1, 6)

    def take_turn(self):
        self._score += self._roll()
        print(f"{self}: {self._score} (rolled a {self._roll()})")

    def __str__(self):
        return f"Player {self.num}"


class LuckyPlayer(Player):
    @staticmethod
    def _roll():
        return randint(3, 6)

    def __str__(self):
        original = super().__str__()
        return original + "*"


def get_player(num):
    if num % 2 == 0:
        return LuckyPlayer(num)
    return Player(num)
