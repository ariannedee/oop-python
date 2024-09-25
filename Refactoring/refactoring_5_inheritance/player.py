from random import randint


class Player:
    def __init__(self, player_num):
        self.num = player_num
        self._score = 0

    @property
    def score(self):
        return self._score

    def take_turn(self):
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
        base_str = super(Player, self).__str__()
        return f"${base_str}$"


def get_player(num):
    if num == 2:
        return LuckyPlayer(num)
    return Player(num)
