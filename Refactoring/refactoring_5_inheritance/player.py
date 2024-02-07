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
        roll = self._roll()
        self._score += roll
        if self.prev_roll == 1 and roll == 1:
            self._score += self.ROLL_BONUS_1S
            print(f"{self}: {self.score} (rolled a {roll}, +10 bonus)")
        else:
            print(f"{self}: {self.score} (rolled a {roll})")
        self.prev_roll = roll

    @staticmethod
    def _roll():
        return randint(1, 6)

    def __str__(self):
        return f"Player {self.num}"

    def __repr__(self):
        return f"Player({self.num})"


class LuckyPlayer(Player):
    @staticmethod
    def _roll():
        return randint(3, 6)

    def __str__(self):
        return super().__str__() + "*"


def get_player(player_num):
    if player_num == 2:
        return LuckyPlayer(player_num)
    return Player(player_num)
