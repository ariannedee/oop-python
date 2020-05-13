from player import LuckyPlayer, Player


class Game:
    def __init__(self, num_players=2, max_die_number=6):
        self.target_score = 50
        self.dice_type = max_die_number
        self.players = []
        for i in range(num_players):
            if i == 1:
                self.players.append(LuckyPlayer())
            else:
                self.players.append(Player())

    def play_game(self):
        while True:
            for player in self.players:
                player.make_move(with_die=self.dice_type)
                if player.score >= self.target_score:
                    print(f'{player} wins!')
                    return player
