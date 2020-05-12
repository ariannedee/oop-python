"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from game import Game

if __name__ == '__main__':
    game = Game(num_players=4, max_die_number=20)
    winner = game.play_game()
    print(f'Congratulations {winner}')
