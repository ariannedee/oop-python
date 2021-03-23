"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from game import Game  # In PyCharm, mark parent directory as Sources Root for imports to work

if __name__ == '__main__':
    game1 = Game(num_players=2, target_score=20)
    game2 = Game(num_players=3, target_score=50)

    game2.play_game()
    game1.play_game()
