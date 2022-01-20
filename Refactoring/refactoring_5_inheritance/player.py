from random import randint


class Player:
    def __init__(self, player_num):
        self._score = 0
        self.num = player_num

    @staticmethod
    def _roll():
        return randint(1, 6)

    @property
    def score(self):
        return self._score

    def make_move(self):
        roll = self._roll()
        self._score += roll
        print(f"{self} score: {self.score} (rolled a {roll})")

    def __str__(self):
        return f"Player {self.num}"

    def __repr__(self):
        return f"{type(self).__name__}({self.num})"


class LuckyPlayer(Player):
    @staticmethod
    def _roll():
        return randint(3, 6)

    def __str__(self):
        player_str = super(Player, self).__str__()
        return f"{player_str} (lucky)"
