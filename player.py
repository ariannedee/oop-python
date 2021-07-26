import random
from random import randint
from as_dict import AsDict


class Player(AsDict):
    def __init__(self, player_num):
        self._score = 0
        self.player_num = player_num

    def take_turn(self):
        roll = self._roll_die()
        self._score += roll
        print(f"{self}: {self._score} (rolled a {roll})")

    @staticmethod
    def _roll_die():
        return randint(1,6)

    def has_won(self):
        return self._score >= 100

    @property
    def score(self):
        return self._score

#    @score.setter
#    def score(self, new_score):
#        raise Exception("Can't set score")

    def __str__(self):
        return f"Player {self.player_num}"

class LuckyPlayer(Player):
    @staticmethod
    def _roll_die():
        return randint(3,6)

    def __str__(self):
        return super().__str__() + "(lucky)"

def get_player(player_num):
    if random.random() > 0.5:
        return Player(player_num)
    return LuckyPlayer(player_num)