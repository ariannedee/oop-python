"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from game import Game

if __name__ == '__main__':
    game = Game(num_players=3, target_score=20)
    game2 = Game(num_players=2, target_score=40)

    game.run()
    game2.run()

    print(game.as_dict())
    for p in game.players:
        print(p.as_dict())

