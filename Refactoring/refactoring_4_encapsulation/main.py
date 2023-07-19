"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from game import Game

if __name__ == '__main__':
    game_1 = Game(num_players=4, target_score=20)
    game_1.start()
    print()
    game_2 = Game(num_players=3, target_score=50)
    game_2.start()
