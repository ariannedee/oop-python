"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.

Object-oriented with a Player object
"""
import random


class Player(object):
    def __init__(self, player_num):
        self.score = 0
        self.player_num = player_num

    def make_move(self):
        dice = random.randint(1, 6)
        print(f'{self} roll a {dice}')
        self.score += dice
        print(f'{self} score: {self.score}')

    def met_goal(self):
        return self.score >= 100

    def __str__(self):
        return f'Player {self.player_num}'


players = []
for i in range(1, 3):
    players.append(Player(i))

print('Start game!')
while True:
    for player in players:
        player.make_move()       # Care about "what", not "how"
        if player.met_goal():
            print(f'{player} won!')
            break
    else:
        continue
    break

print()
for player in players:
    print(f'{player} score: {player.score}')
