"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from random import randint


class Player:
    def __init__(self, num, score=0):
        self.num = num
        self.score = score

    def take_turn(self):
        roll = randint(1, 6)
        self.score += roll
        print(f"{self}: {self.score} (rolled a {roll})")

    def has_won(self, target_score):
        return self.score >= target_score

    def __str__(self):
        return f"Player {self.num}"

    def __repr__(self):
        return f"Player({self.num}, score={self.score})"


def play_game(num_players=2, target_score=100):
    players = [Player(i+1) for i in range(num_players)]

    while True:
        for player in players:
            player.take_turn()

            if player.has_won(target_score):
                print(f'{player} wins!')
                print(players)
                return


if __name__ == '__main__':
    print("--- START GAME 1 ---")
    play_game(3, 50)
    print("--- END GAME 1 ---")
    print("--- START GAME 2 ---")
    play_game(4, 60)
    print("--- END GAME 2 ---")
