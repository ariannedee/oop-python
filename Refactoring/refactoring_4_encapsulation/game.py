from player import Player


class Game:
    def __init__(self, num_players=2, target_score=100):
        self.target_score = target_score
        self.players = []
        for i in range(num_players):
            self.players.append(Player(i + 1))

    def play_game(self):
        while True:
            for player in self.players:
                player.take_turn()
                if self.game_over():
                    return

    def game_over(self):
        for player in self.players:
            if player.did_win_game(self.target_score):
                print(f"{player} wins")
                return True
        return False
