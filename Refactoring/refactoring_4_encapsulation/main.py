"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from game import Game  # In PyCharm, mark parent directory as Sources Root for imports to work

if __name__ == '__main__':
    my_game = Game(3, win_score=50)
    my_game.run_game()

    print('------- GAME 1 OVER --------')

    another_game = Game(2)
    another_game.run_game()

    print('------- GAME 2 OVER --------')
