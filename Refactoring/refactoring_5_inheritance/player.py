from random import randint


class Player:
    def __init__(self, num):
        self.num = num
        self._score = 0
        self.__private = True

    @property
    def score(self):
        return self._score

    def do_turn(self):
        roll = self._roll()
        self._score += roll
        print(f"{self}: {self.score} (rolled a {roll})")

    @staticmethod
    def _roll():
        return randint(1, 6)

    def __str__(self):
        return f"Player {self.num}"


class LuckyPlayer(Player):
    @staticmethod
    def _roll():
        return randint(3, 6)

    def __str__(self):
        original_string = super().__str__()
        return original_string + "*"


def get_player(num):
    if num % 2 == 1:
        return Player(num)
    return LuckyPlayer(num)