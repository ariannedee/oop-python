from random import randint


class Player:
    def __init__(self, num):
        self._score = 0
        self.num = num

    def take_turn(self):
        roll = randint(1, 6)
        self._score += roll
        print(f"{self}: {self.score} (rolled a {roll})")

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if value < 0:
            raise ValueError("Can't set score below 0")
        self._score = value

    def __str__(self):
        return f"Player {self.num}"

    def __repr__(self):
        pass
