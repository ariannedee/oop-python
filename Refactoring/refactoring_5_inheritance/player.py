from random import randint


class Player:
    def __init__(self, player_num, score=0):
        self.num = player_num
        self._score = score

    def take_turn(self):
        roll = self._roll()
        self._score += roll
        print(f"{self}: {self._score} (rolled a {roll})")

    @staticmethod
    def _roll():
        return randint(1, 6)

    @property
    def score(self):
        return self._score

    def __str__(self):
        return f"Player {self.num}"

    def __repr__(self):
        return f"{type(self).__name__}({self.num}, score={self._score})"


class LuckyPlayer(Player):
    @staticmethod
    def _roll():
        return randint(3, 6)

    def __str__(self):
        return f"({super().__str__()})"


def get_player(num):
    if num == 3:
        return LuckyPlayer(num)
    return Player(num)
