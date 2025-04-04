from player import Player


class Game:
    counter = 0

    def __init__(self, num_players=2, target_score=100):
        Game.counter += 1
        self.players = [Player(i + 1) for i in range(num_players)]
        self.target_score = target_score
        self.num = Game.counter

    def run(self):
        print(f"----- {self} start -----".upper())

        while True:
            for player in self.players:
                player.take_turn()
            if self.game_over():
                print(f"{self.winner()} wins!")
                print(f"----- {self} end -----".upper())
                return

    def game_over(self):
        for player in self.players:
            if player.score >= self.target_score:
                return True
        return False

    def winner(self):
        high_score = 0
        cur_winner = None
        for player in self.players:
            if player.score > high_score:
                high_score = player.score
                cur_winner = player
        return cur_winner

    def __str__(self):
        return f"Game {self.num}"
