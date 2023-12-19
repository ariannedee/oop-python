from player import Player


class Game:
    counter = 0

    def __init__(self, num_players=2, target_score=100):
        self.players = [Player(i + 1) for i in range(num_players)]
        self.target_score = target_score
        Game.counter += 1
        self.num = Game.counter

    def game_over(self):
        for player in self.players:
            if player.score >= self.target_score:
                return True
        return False

    def get_winner(self):
        max_score = 0
        max_player = None
        for player in self.players:
            if player.score >= max_score:
                max_score = player.score
                max_player = player
        return max_player

    def run(self):
        print(f"---- {self} start ----".upper())
        while True:
            for player in self.players:
                player.do_turn()
            if self.game_over():
                print(f"{self.get_winner()} wins!")
                print(f"---- {self} end ----".upper())
                return

    def __str__(self):
        return f"Game {self.num}"
