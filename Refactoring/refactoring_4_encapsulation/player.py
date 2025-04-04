from random import randint


class Player:
    def __init__(self, num, score=0):
        self.num = num
        self._score = score

    @property
    def score(self):
        return self._score

    def take_turn(self):
        roll = randint(1, 6)
        self._score += roll
        print(f"{self}: {self.score} (rolled a {roll})")

    def __str__(self):
        return f"Player {self.num}"

    def __repr__(self):
        return f"Player({self.num}, score={self.score})"
