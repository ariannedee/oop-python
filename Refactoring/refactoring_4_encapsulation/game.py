from player import Player


class Game:
    counter = 0

    def __init__(self, num_players, target_score=100):
        self.target_score = target_score
        self.players = [Player(i + 1) for i in range(num_players)]
        Game.counter += 1
        self.num = Game.counter

    def start(self):
        print(f'---- {self} start ----')

    def end(self):
        print(f'---- {self} end ----')

    def run(self):
        self.start()
        self.take_turns()
        self.end()

    def take_turns(self):
        while True:
            for player in self.players:
                player.take_turn()
            if self.game_over():
                print(f'{self.winner} wins!')
                return

    def game_over(self):
        for player in self.players:
            if player.score >= self.target_score:
                return True
        return False

    @property
    def winner(self):
        max_score = -1
        max_player = None
        for player in self.players:
            if player.score > max_score:
                max_score = player.score
                max_player = player
        return max_player

    def __str__(self):
        return f'Game {self.num}'
