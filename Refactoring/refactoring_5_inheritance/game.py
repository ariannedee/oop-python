from player import get_player


class Game:
    _counter = 0

    def __init__(self, num_players=2, target_score=100):
        Game._counter += 1
        self.num = Game._counter
        self.target_score = target_score
        self.players = []
        for i in range(num_players):
            self.players.append(get_player(i + 1))

    def run(self):
        self._game_start()
        self._game_play()
        self._game_end()

    def _game_start(self):
        print(f"--- {self} START ---".upper())

    def _game_play(self):
        while True:
            for player in self.players:
                player.take_turn()

            if self.game_over():
                print(f"{self.winner} wins!")
                return

    def _game_end(self):
        print(f"--- {self} END ---".upper())

    def game_over(self):
        for player in self.players:
            if player._score >= self.target_score:
                return True
        return False

    @property
    def winner(self):
        winner = None
        high_score = 0
        for player in self.players:
            if player._score > high_score:
                winner = player
                high_score = player._score
        return winner

    def __str__(self):
        return f"Game {self.num}"

    def __repr__(self):
        return f"Game(num_players={len(self.players)}, target_score={self.target_score})"
