from random import randint


class Player:
    def __init__(self, player_num):
        self.num = player_num
        self._score = 0

    @property
    def score(self):
        return self._score

    def take_turn(self):
        roll = self.roll_die()
        self._score += roll
        print(f"{self}: {self._score} (rolled a {roll})")

    @staticmethod
    def roll_die():
        return randint(1, 6)

    def __str__(self):
        return f"{type(self).__name__} {self.num}"

    def __repr__(self):
        return f"{type(self).__name__}({self.num})"


class LuckyPlayer(Player):
    @staticmethod
    def roll_die():
        return randint(3, 6)


def get_player(num):
    if num % 2 == 1:
        return Player(num)
    return LuckyPlayer(num)
