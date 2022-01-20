from player import Player


class Game:
    counter = 0

    def __init__(self, num_players, target_score=100):
        Game.counter += 1
        self.game_num = Game.counter
        self.players = [Player(i + 1) for i in range(num_players)]
        self.target_score = target_score

    def player_has_won(self, player):
        return player.score >= self.target_score

    def run(self):
        print(f"------ {self} start --------")

        while True:
            for player in self.players:
                player.make_move()

                if self.player_has_won(player):
                    print(f"{player} wins!")
                    print(f"------ {self} end --------")
                    return

    def __str__(self):
        return f"Game {self.game_num}"

    def __repr__(self):
        return f"Game({len(self.players)})"
