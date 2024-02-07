from player import Player


class Game:
    counter = 0

    def __init__(self, num_players=2, target_score=100):
        self.target_score = target_score
        self.players = [Player(i + 1) for i in range(num_players)]
        Game.counter += 1
        self.num = Game.counter

    def run(self):
        print(f"---- {self} START ----".upper())
        self._take_turns()
        print(f"---- {self} END ----".upper())

    def check_if_game_over(self):
        game_over = False
        winner = None
        high_score = 0
        for player in self.players:
            if player.score > high_score:
                winner = player
                high_score = player.score
            if player.score >= self.target_score:
                game_over = True
        return game_over, winner

    def _take_turns(self):
        while True:
            for player in self.players:
                player.take_turn()
            game_over, winner = self.check_if_game_over()
            if game_over:
                print(f"{winner} wins!")
                return

    def __str__(self):
        return f"Game {self.num}"
