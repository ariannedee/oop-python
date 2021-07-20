from random import randint


class Player:
    def __init__(self, player_num):
        self._score = 0
        self.player_num = player_num

    def take_turn(self):
        roll = randint(1, 6)
        self._score += roll
        print(f"{self}: {self._score} (rolled a {roll})")

    def has_won(self):
        return self._score >= 100

    @property
    def score(self):
        return self._score

    def __str__(self):
        return f"Player {self.player_num}"
