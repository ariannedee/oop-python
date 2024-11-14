from player import get_player


class Game:
    counter = 0

    def __init__(self, num_players=2, target_score=100):
        self.players = [get_player(i + 1) for i in range(num_players)]
        self.target_score = target_score
        Game.counter += 1
        self.id = self.counter

    def play_game(self):
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
        cur_winner = None
        high_score = 0

        for player in self.players:
            if player.score > high_score:
                cur_winner = player
                high_score = player.score

        return cur_winner

    def run(self):
        print(f"---- {str(self).upper()} start ----")
        self.play_game()
        print(f"---- {str(self).upper()} end ----")

    def __str__(self):
        return f"Game {self.id}"
