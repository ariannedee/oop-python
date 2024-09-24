from random import randint


class Player:
    def __init__(self, player_num):
        self.num = player_num
        self._score = 0

    @property
    def score(self):
        return self._score

    def take_turn(self):
        roll = randint(1, 6)
        self._score += roll
        print(f"{self}: {self.score} (rolled a {roll})")

    def __str__(self):
        return f"Player {self.num}"
