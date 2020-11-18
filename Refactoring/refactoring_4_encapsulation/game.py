from player import Player


class Game:
    def __init__(self, num_players, target_score=100):
        self.target_score = target_score
        self.players = []
        for i in range(num_players):
            self.players.append(Player(i + 1))

    def player_won(self, player):
        return player.score >= self.target_score

    def run_game(self):
        while True:
            for player in self.players:
                player.take_turn()
                if self.player_won(player):
                    print(f"{player} wins!")
                    return
