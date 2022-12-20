from random import randint


class Player:
    def __init__(self, num):
        self.num = num
        self._score = 0

    def take_turn(self):
        roll = randint(1, 6)
        self._score += roll
        print(f"{self}: {self._score} (rolled a {roll})")

    @property
    def score(self):
        return self._score

    def __str__(self):
        return f"Player {self.num}"
