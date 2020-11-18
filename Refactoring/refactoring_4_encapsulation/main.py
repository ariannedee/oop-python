"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from game import Game  # In PyCharm, mark parent directory as Sources Root for imports to work

Game(num_players=4, target_score=20).run_game()
print("---------- END GAME 1 ---------")
Game(num_players=2, target_score=30).run_game()
print("---------- END GAME 2 ---------")
