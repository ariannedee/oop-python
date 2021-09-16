from player import get_player


class Game:
    counter = 0

    def __init__(self, num_players, target_score=100):
        self.players = [get_player(i) for i in range(1, num_players + 1)]
        self.target_score = target_score
        Game.counter += 1
        self.game_num = Game.counter

    def run_game(self):
        print()
        print(f"{self} started")
        while True:
            for player in self.players:
                player.take_turn()
            self.game_state()
            if self.game_over():
                winners = self.get_winners()
                if len(winners) == 1:
                    print(f"{winners[0]} wins!")
                else:
                    print(f"{', '.join(winners)} win!")
                return

    def game_over(self):
        for player in self.players:
            if player.score >= self.target_score:
                return True
        return False

    def get_winners(self):
        return [
            str(player) for player in self.players
            if player.score >= self.target_score
        ]

    def game_state(self):
        max_score = 0
        in_lead = None
        for player in self.players:
            if player.score > max_score:
                in_lead = player

        print(f"{in_lead} is winning with {in_lead.score}")

    def __str__(self):
        return f"Game {self.game_num}"
