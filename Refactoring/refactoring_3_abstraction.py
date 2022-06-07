"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from random import randint


class Player:
    def __init__(self, num):
        self.score = 0
        self.num = num

    def make_move(self):
        roll = randint(1, 6)
        self.score += roll
        print(f'{self} rolled a {roll} ({self.score})')

    def has_won(self):
        return self.score >= 100

    def __str__(self):
        return f'Player {self.num}'

    def __repr__(self):
        return f'Player({self.num})'


def play_game(num_players=2):
    players = [Player(i + 1) for i in range(num_players)]
    while True:
        for player in players:
            player.make_move()
            if player.has_won():
                print(f'{player} wins!')
                return


if __name__ == '__main__':
    print("-- Game 1 start --")
    play_game(num_players=3)
    print("-- Game 1 end --")
    print("-- Game 2 start --")
    play_game(num_players=4)
    print("-- Game 2 end --")
