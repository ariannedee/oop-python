from random import randint


class MethodNotAllowed(BaseException):
    pass


class Player:
    def __init__(self, player_num):
        self._score = 0
        self.player_num = player_num

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        raise MethodNotAllowed()

    def take_turn(self):
        roll = self._roll_die()
        self._score += roll
        print(f"{self}: {self._score} (rolled a {roll})")

    @staticmethod
    def _roll_die():
        return randint(1, 6)

    def has_won(self, target_score):
        return self._score >= target_score

    def __str__(self):
        return f"Player {self.player_num}"

    def __repr__(self):
        return f"{type(self).__name__} {self.player_num}: {self._score}"


class LuckyPlayer(Player):
    @staticmethod
    def _roll_die():
        return randint(3, 6)

    def __str__(self):
        player_str = super().__str__()
        return player_str + " (lucky)"
