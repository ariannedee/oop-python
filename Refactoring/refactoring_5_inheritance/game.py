from player import get_player


class Game:
    counter = 0

    def __init__(self, num_players=2, target_score=100):
        self.target_score = target_score
        self.players = [get_player(i + 1) for i in range(num_players)]
        Game.counter += 1
        self.num = Game.counter

    def start(self):
        print(f"---- {self} START ----")
        self._run_game()
        print(f"---- {self} END ----")

    def game_over(self):
        for player in self.players:
            if player._score >= self.target_score:
                return True

    def get_winner(self):
        winner = None
        score = 0
        for player in self.players:
            if player._score > score:
                winner = player
                score = player._score
        return winner

    def _run_game(self):
        while True:
            for player in self.players:
                player.take_turn()

            if self.game_over():
                winner = self.get_winner()
                print(f"{winner} wins!")
                return

    def __str__(self):
        return f"Game {self.num}"

    def __repr__(self):
        return f"Game({len(self.players)}, {self.target_score})"
