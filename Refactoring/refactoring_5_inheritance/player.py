from random import randint


class Player:
    def __init__(self, num):
        self._score = 0
        self.num = num

    def take_turn(self):
        self._score += self._roll()
        print(f"{self}: {self._score} (rolled a {self._roll()})")

    @staticmethod
    def _roll():
        return randint(1, 6)

    @property
    def score(self):
        return self._score

    def __str__(self):
        return f"{type(self).__name__} {self.num}"

    def __repr__(self):
        return f"{type(self).__name__}({self.num}, score={self._score})"


class LuckyPlayer(Player):
    @staticmethod
    def _roll():
        return randint(3, 6)


def get_player(num):
    if num == 2:
        return LuckyPlayer(num)
    return Player(num)
