import random


class Player:
    def __init__(self, player_num):
        self.player_num = player_num
        self._score = 0

    @staticmethod
    def roll_die():
        return random.randint(1, 6)

    def take_turn(self):
        roll = self.roll_die()
        self._score += roll
        print(f"{self} score: {self._score} (rolled a {roll})")

    @property
    def score(self):
        return self._score

    def __str__(self):
        return f"Player {self.player_num}"

    def __repr__(self):
        return str(self)


class LuckyPlayer(Player):
    @staticmethod
    def roll_die():
        return random.randint(3, 6)

    def __str__(self):
        return f"{super().__str__()} (lucky)"
