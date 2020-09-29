from player import Player


class Game:
    def __init__(self, num_players, win_score=100):
        self.win_score = win_score
        self.players = []
        for num in range(num_players):
            self.players.append(Player(num + 1))

    def run_game(self):
        while True:
            for player in self.players:
                player.take_turn()
                if self.has_won(player):
                    print(f"{player} wins!")
                    return

    def has_won(self, player):
        return player.score >= self.win_score
