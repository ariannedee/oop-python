from player import get_player


class Game:
    counter = 0

    def __init__(self, num_players, target_score=100):
        self.target_score = target_score
        self.players = [get_player(i + 1) for i in range(num_players)]
        Game.counter += 1
        self.number = Game.counter

    def __str__(self):
        return f"Game {self.number}"

    def __repr__(self):
        return f"Game({len(self.players)}, {self.target_score})"

    def start_game(self):
        print(f"--- {self} START ---")

    def end_game(self):
        print(f"--- {self} END ---\n")

    def run_game(self):
        while True:
            for player in self.players:
                player.take_turn()
                if self.is_game_over(player):
                    print(f"{player} wins!")
                    return

    def is_game_over(self, player):
        return player.score >= self.target_score

    def start(self):
        self.start_game()
        self.run_game()
        self.end_game()
