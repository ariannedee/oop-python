from random import randint


class Player:
    ROLL_BONUS_1S = 10

    def __init__(self, num):
        self.num = num
        self._score = 0
        self.prev_roll = None

    @property
    def score(self):
        return self._score

    def take_turn(self):
        roll = randint(1, 6)
        self._score += roll
        if self.prev_roll == 1 and roll == 1:
            self._score += self.ROLL_BONUS_1S
            print(f"{self}: {self.score} (rolled a {roll}, +10 bonus)")
        else:
            print(f"{self}: {self.score} (rolled a {roll})")
        self.prev_roll = roll

    def __str__(self):
        return f"Player {self.num}"

    def __repr__(self):
        return f"Player({self.num})"
