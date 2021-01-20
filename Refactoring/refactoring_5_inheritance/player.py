from random import randint


class AsDictMixin:
    def as_dict(self):
        return {
            'id': id(self),
            'object': self
        }


class Player(AsDictMixin):
    def __init__(self, player_number):
        self.score = 0
        self.player_number = player_number

    def take_turn(self):
        roll = self._roll_die()
        self.score += roll
        print(f"{self}: {self.score} (rolled a {roll})")

    @staticmethod
    def _roll_die():
        return randint(1, 6)

    def did_win_game(self, target_score):
        return self.score >= target_score

    def __str__(self):
        return f'Player {self.player_number}'


class LuckyPlayer(Player):
    @staticmethod
    def _roll_die():
        return randint(3, 6)

    def __str__(self):
        return f'Player {self.player_number} (lucky)'
