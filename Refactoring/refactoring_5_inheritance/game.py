from player import get_player


class Game:
    counter = 0

    def __init__(self, num_players=2, target_score=100):
        self.target_score = target_score
        self.players = [get_player(i + 1) for i in range(num_players)]
        Game.counter += 1
        self.num = Game.counter

    def __str__(self):
        return f"Game {self.num}"

    def start(self):
        print(f"--- {self} START ---".upper())
        self._run()
        print(f"--- {self} END ---".upper())

    def _run(self):
        while True:
            for player in self.players:
                player.take_turn()

            if self.is_over():
                print(f"{self.winner} wins!")
                return

    def is_over(self):
        for player in self.players:
            if player.score >= self.target_score:
                return True
        return False

    @property
    def winner(self):
        win_player = None
        max_score = -1
        for player in self.players:
            if player.score > max_score:
                win_player = player
                max_score = player.score
        return win_player
