from random import randint


class Player:
    def __init__(self, player_number):
        self.score = 0
        self.player_number = player_number

    def take_turn(self):
        roll = self._roll_die()
        self.score += roll
        print(f"Player {self.player_number}: {self.score} (rolled a {roll})")

    @staticmethod
    def _roll_die():
        return randint(1, 6)

    def did_win_game(self, target_score):
        return self.score >= target_score

    def __str__(self):
        return f'Player {self.player_number}'
