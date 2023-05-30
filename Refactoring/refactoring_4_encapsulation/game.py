from player import Player


class Game:
    def __init__(self, game_num, num_players=2, target_score=100):
        self.num = game_num
        self.target_score = target_score
        self.players = [Player(i + 1) for i in range(num_players)]

    def run(self):
        print(f"{self} START")
        self.run_rounds()
        print(f"{self} END")

    def run_rounds(self):
        while True:
            for player in self.players:
                player.take_turn()
            if self.game_over():
                print(f"{self.winner} wins!")
                return

    def game_over(self):
        return any(filter(lambda player: player.score > self.target_score, self.players))

    @property
    def winner(self):
        winner = None
        max_score = 0
        for player in self.players:
            if player.score > max_score:
                winner = player
                max_score = player.score
        return winner

    def __str__(self):
        return f"Game {self.num}"
