from random import randint


class Player:
    def __init__(self, num, score=0):
        self.num = num
        self._score = score

    @property
    def score(self):
        return self._score

    @staticmethod
    def _roll():
        return randint(1, 6)

    def take_turn(self):
        roll = self._roll()
        self._score += roll
        print(f"{self}: {self.score} (rolled a {roll})")

    def __str__(self):
        return f"Player {self.num}"

    def __repr__(self):
        return f"{type(self).__name__}({self.num}, score={self.score})"


class LuckyPlayer(Player):
    def __init__(self, minimum_roll=3, *args, **kwargs):
        print(args)
        print(kwargs)
        super().__init__(*args, **kwargs)
        self.min_roll = minimum_roll

    def _roll(self):
        return randint(self.min_roll, 6)

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}*"


def get_player(num):
    if num == 2:
        return LuckyPlayer(2, num, 20)
    else:
        return Player(num)
