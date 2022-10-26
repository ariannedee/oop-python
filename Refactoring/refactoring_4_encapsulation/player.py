from random import randint


class Player:
    def __init__(self, number):
        self._score = 0
        self.number = number

    @property
    def score(self):
        return self._score

    def take_turn(self):
        roll = randint(1, 6)
        self._score += roll
        print(f"{self} rolled a {roll} (total: {self.score})")

    def __str__(self):
        return f"Player {self.number}"

    def __repr__(self):
        return f"Player({self.number})"
