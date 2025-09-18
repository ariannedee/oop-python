"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 50 wins.
"""
from game import Game

if __name__ == '__main__':
    Game(3, 40).run()
    Game(4, 30).run()
