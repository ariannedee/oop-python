"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.

Object-oriented with a Player and Game objects
"""
import random


class Player(object):
    _target_score = 100  # hidden and "private"

    def __init__(self, player_num):
        self.score = 0
        self.player_num = player_num

    def make_move(self):
        dice = random.randint(1, 6)
        print(f'{self} roll a {dice}')
        self.score += dice
        print(f'{self} score: {self.score}')

    def met_goal(self):
        return self.score >= self._target_score

    def __str__(self):
        return f'Player {self.player_num}'


class Game(object):
    def __init__(self, num_players):
        self.players = []
        for i in range(1, num_players+1):
            self.players.append(Player(i))

    def start_game(self):
        print('Start game!')
        while True:
            for player in self.players:
                player.make_move()
                if player.met_goal():
                    print(f'{player} won!')
                    print()
                    return

    def final_score(self):
        for player in self.players:
            print(f'{player} score: {player.score}')


game = Game(num_players=4)
game.start_game()
game.final_score()

for i in range(2, 5):
    game = Game(num_players=i)
    game.start_game()
    game.final_score()
