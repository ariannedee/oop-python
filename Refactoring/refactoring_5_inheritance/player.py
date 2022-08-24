from random import randint


class Player:
    count = 0

    def __init__(self, player_num):
        self.num = player_num
        self._score = 0
        Player.count += 1

    def take_turn(self):
        roll = self._roll()
        self._score += roll
        print(f'{self} rolled a {roll} ({self._score})')

    @staticmethod
    def _roll():
        return randint(1, 6)

    @property
    def score(self):
        return self._score

    def __str__(self):
        return f'Player {self.num}'

    def __repr__(self):
        return f'Player({self.num})'


class LuckyPlayer(Player):
    @staticmethod
    def _roll():
        return randint(3, 6)

    def __str__(self):
        return f'{super().__str__()} (lucky)'


def create_player(player_num):
    if Player.count % 3 == 0:
        return LuckyPlayer(player_num)
    return Player(player_num)
