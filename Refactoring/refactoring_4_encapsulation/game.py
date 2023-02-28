from player import Player


class Game:
    def __init__(self, num_players=2, target_score=100):
        self.target_score = target_score
        self.players = [Player(i + 1) for i in range(num_players)]

    def run_game(self):
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
        max_score = 0
        for player in self.players:
            if player.score > max_score:
                winner = player
        return winner
