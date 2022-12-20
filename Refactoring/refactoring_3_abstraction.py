"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
from random import randint

class Player:
    def __init__(self, num):
        self.num = num
        self.score = 0

    def take_turn(self):
        roll = randint(1, 6)
        self.score += roll
        print(f"{self}: {self.score} (rolled a {roll})")

    def __str__(self):
        return f"Player {self.num}"

game = 0


def run_game(num_players, target_score=100):
    global game
    game += 1
    players = [Player(i+1) for i in range(num_players)]
    print(f"----- GAME {game} START -----")

    while True:
        for player in players:
            player.take_turn()
            if player.score >= target_score:
                print(f"{player} wins!")
                print(f"----- GAME {game} END -----")
                return


if __name__ == '__main__':
    run_game(3, 50)
    run_game(4, 60)
