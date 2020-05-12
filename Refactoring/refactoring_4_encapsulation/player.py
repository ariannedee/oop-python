import random


class Player:
    num_players = 0

    def __init__(self):
        Player.num_players += 1
        self.score = 0
        self.player_number = Player.num_players

    def _roll_die(self, dice_number):
        die = random.randint(1, dice_number)
        print(f'{self} rolled a {die}')
        return die

    def make_move(self, with_die):
        self.score += self._roll_die(with_die)
        print(f'{self}: {self.score}')

    def __str__(self):
        return f'Player {self.player_number}'


if __name__ == '__main__':
    dummy_player = Player()
    for i in range(1000):
        die = dummy_player._roll_die(6)
        assert 1 <= die <= 6
