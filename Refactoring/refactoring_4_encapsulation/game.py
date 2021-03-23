from player import Player


class Game:
    counter = 0

    def __init__(self, num_players, target_score=100):
        self.target_score = target_score
        self.players = [Player(i + 1) for i in range(num_players)]  # List comprehension
        Game.counter += 1
        self.game_num = Game.counter

    def __del__(self):
        Game.counter -= 1

    def play_game(self):
        self._game_start()
        self._game_play()
        self._game_end()

    def _game_play(self):
        while True:
            for player in self.players:
                player.take_turn()
                if player.has_won(self.target_score):
                    print(f"{player} wins")
                    return

    def _game_start(self):
        print(f"{self} start")

    def _game_end(self):
        print(f"{self} is over\n")

    def __str__(self):
        return f"Game {self.game_num}"

    def __repr__(self):
        return f"Game {self.game_num}: {len(self.players)} players"

