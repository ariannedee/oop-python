from player import Player


class Game:
    counter = 0

    def __init__(self, num_players, target_score=100):
        self.players = [Player(i) for i in range(1, num_players + 1)]
        Game.counter += 1
        self.num = Game.counter
        self.target_score = target_score

    def start_game(self):
        print(f"------ START GAME {self.num}-------")
        print(f"Num players: {len(self.players)}")
        print(f"Target score: {self.target_score}")

    def end_game(self):
        print(f"------ END GAME {self.num }-------")

    def game_over(self, player):
        return player.score >= self.target_score

    def do_turns(self):
        while True:
            for player in self.players:
                player.take_turn()

                if self.game_over(player):
                    print(f'{player} wins!')
                    return

    def run_game(self):
        self.start_game()
        self.do_turns()
        self.end_game()
