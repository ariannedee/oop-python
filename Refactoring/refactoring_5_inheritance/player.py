from random import randint


class Player:
    def __init__(self, num, score=0):
        self.num = num
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if value < 0:
            raise ValueError("Score cannot be negative")
        self._score = value

    def take_turn(self):
        roll = self._roll()
        self._score += roll
        print(f"{self}: {self.score} (rolled a {roll})")

    @staticmethod
    def _roll():
        return randint(1, 6)

    def __str__(self):
        return f"Player {self.num}"

    def __repr__(self):
        return f"Player({self.num}, {self.score})"


class LuckyPlayer(Player):
    @staticmethod
    def _roll():
        return randint(3, 6)

    def __str__(self):
        return super().__str__() + "*"



def get_player(num):
    if num == 2:
        return LuckyPlayer(num)
    return Player(num)
