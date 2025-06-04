from player import Player


class Game:
    counter = 0

    def __init__(self, num_players=2, target_score=100):
        self.target_score = target_score
        Game.counter += 1
        self.num = Game.counter

        self.players: list[Player] = [Player(i + 1) for i in range(num_players)]

    def run(self):
        print(f"---- {self} START ----".upper())
        self._take_turns()
        print(f"---- {self} END ----".upper())

    def _take_turns(self):
        while True:
            for player in self.players:
                player.take_turn()
            if self.game_over():
                print(f"{self.winner} wins!")
                return

    def game_over(self):
        for player in self.players:
            if player.score >= self.target_score:
                return True
        return False

    @property
    def winner(self):
        winner = None
        high_score = 0
        for player in self.players:
            if player.score >= high_score:
                high_score = player.score
                winner = player
        return winner

    def __str__(self):
        return f"Game {self.num}"


if __name__ == '__main__':
    game = Game()