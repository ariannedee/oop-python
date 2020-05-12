"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
import random


class Player:
    def __init__(self, player_number):
        self.score = 0
        self.player_number = player_number

    def roll_die(self):
        die = random.randint(1, 6)
        print(f'{self} rolled a {die}')
        return die

    def make_move(self):
        self.score += self.roll_die()
        print(f'{self}: {self.score}')

    @property
    def has_won(self):
        return self.score >= 100

    def __str__(self):
        return f'Player {self.player_number}'


def play_game(num_players=2):
    players = []
    for i in range(num_players):
        players.append(Player(i + 1))

    while True:
        for player in players:
            player.make_move()
            if player.has_won:
                print(f'{player} wins!')
                return


if __name__ == '__main__':
    play_game(num_players=3)
