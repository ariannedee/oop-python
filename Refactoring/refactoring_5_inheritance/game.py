from player import get_player


class Game:
    counter = 0

    def __init__(self, num_players=2, target_score=100):
        self.target_score = target_score
        self.players = [get_player(i + 1) for i in range(num_players)]
        Game.counter += 1
        self.num = Game.counter

    def run_game(self):
        print(f"=== {str(self).upper()} START ===")
        self._take_turns()
        print(f"=== {self} END ===".upper())

    def _take_turns(self):
        while True:
            for player in self.players:
                player.take_turn()
                if player.score >= self.target_score:
                    print(f"{player} wins!")
                    return

    def __str__(self):
        return f"Game {self.num}"
