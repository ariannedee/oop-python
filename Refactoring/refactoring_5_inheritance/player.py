from random import randint


class Player:
    def __init__(self, number):
        self._score = 0
        self.number = number

    @property
    def score(self):
        return self._score

    def take_turn(self):
        roll = self.roll()
        self._score += roll
        print(f"{self} rolled a {roll} (total: {self.score})")

    @staticmethod
    def roll():
        return randint(1, 6)

    def __str__(self):
        return f"PLAYER {self.number}"

    def __repr__(self):
        return f"Player({self.number})"


class LuckyPlayer(Player):
    @staticmethod
    def roll():
        return randint(3, 6)

    def __str__(self):
        player_str = super().__str__()
        return f"{player_str} (lucky)"


def get_player(num):
    if num % 2 == 0:
        return LuckyPlayer(num)
    return Player(num)
