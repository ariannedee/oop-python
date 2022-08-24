"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from random import randint


class Player:
    def __init__(self, player_num):
        self.num = player_num
        self.score = 0

    def take_turn(self):
        roll = randint(1, 6)
        self.score += roll
        print(f'{self} rolled a {roll} ({self.score})')

    def has_won(self):
        return self.score >= 100

    def __str__(self):
        return f'Player {self.num}'

    def __repr__(self):
        return f'Player({self.num})'


def run_game(num_players=2):
    players = [Player(i) for i in range(1, num_players + 1)]
    print("------ START GAME -------")
    while True:
        for player in players:
            player.take_turn()

            if player.has_won():
                print(f'{player} wins!')
                print("------ END GAME -------")
                return


if __name__ == '__main__':
    run_game(2)
    run_game(3)
