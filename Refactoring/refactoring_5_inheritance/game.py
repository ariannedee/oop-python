from player import get_player


class Game:
    counter = 0

    def __init__(self, num_players, target_score=100):
        self.players = [get_player(i + 1) for i in range(num_players)]
        self.target_score = target_score
        Game.counter += 1
        self.num = Game.counter

    def run_game(self):
        self._game_start()

        while True:
            for player in self.players:
                player.take_turn()
                if self.game_over(player):
                    print(f"{player} wins!")
                    self._game_end()
                    return

    def _game_end(self):
        print(f"----- {str(self).upper()} END -----")

    def _game_start(self):
        print(f"----- {str(self).upper()} START -----")

    def game_over(self, player):
        return player.score >= self.target_score

    def __str__(self):
        return f'Game {self.num}'
