from player import get_player, Player


class Game:
    counter = 0

    def __init__(self, num_players=2, target_score=50):
        Game.counter += 1
        self.num = Game.counter
        self.target_score = target_score
        self.players: list[Player] = [get_player(i + 1) for i in range(num_players)]

    def run(self):
        print(f"------ {self} START ------".upper())
        self._take_turns()
        print(f"------ {self} END ------".upper())

    def _take_turns(self):
        while True:
            for player in self.players:
                player.take_turn()

            if self.game_is_over():
                print(f"{self.winner} wins!")
                print(self.players)
                return

    def player_won(self, player):
        return player.score >= self.target_score

    def game_is_over(self):
        for player in self.players:
            if player.score >= self.target_score:
                return True
        return False

    @property
    def winner(self):
        max_score = 0
        max_player = None

        for player in self.players:
            if player.score > max_score:
                max_score = player.score
                max_player = player

        return max_player

    def __str__(self):
        return f"Game {self.num}"

    def __repr__(self):
        return f"Game({len(self.players)}, {self.target_score})"
