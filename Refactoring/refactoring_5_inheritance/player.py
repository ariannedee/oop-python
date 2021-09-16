from random import randint, random


class Player(object):
    def __init__(self, player_num):
        self.player_num = player_num
        self._score = 0

    def take_turn(self):
        player_roll = self._roll()
        self._score += player_roll
        print(f"{self} score is {self._score} (rolled a {player_roll})")

    @staticmethod
    def _roll():
        return randint(1, 6)

    @property
    def score(self):
        return self._score

    def __str__(self):
        return f"Player {self.player_num}"

    def __repr__(self):
        return f"{type(self).__name__}({self.player_num})"


class LuckyPlayer(Player):
    @staticmethod
    def _roll():
        return randint(3, 6)

    def __str__(self):
        string = super().__str__()
        return string + " (lucky)"


def get_player(player_num):
    if random() > 0.5:
        return LuckyPlayer(player_num)
    return Player(player_num)
