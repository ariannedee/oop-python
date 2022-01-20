"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from game import Game  # In PyCharm, mark parent directory as Sources Root for imports to work

if __name__ == '__main__':
    game_1 = Game(num_players=4, target_score=20)
    game_2 = Game(num_players=3)

    game_2.run()
    game_1.run()
