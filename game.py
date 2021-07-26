from player import get_player
from as_dict import AsDict

class Game(AsDict):
    def __init__(self, num_players, target_score=100):
        self.target_score = target_score
        self.players = [get_player(i + 1) for i in range(num_players)]
        self._game_over = False
        self._winner = None

    def run_round(self):
        for player in self.players:
            player.take_turn()
            if self._player_has_won(player):
                self._winner = player
                self._game_over = True

    def _player_has_won(self, player): ## By putting _ we can make the module private such that when you write game. in game_refactoring4.py _player_has_won module is not visible. But you can stil call them..  But if you use two underscore __
        return player.score >= self.target_score

    def _game_start(self):
        print(f"Start game: {self}")

    def _game_end(self):
        print(f"{self._winner} wins!")
        print("--------------------")

    def run(self):
        self._game_start()
        while True:
            self.run_round()
            if self._game_over:
                self._game_end()
                return

    def __str__(self):
        return f"{len(self.players)}--player game to {self.target_score}"