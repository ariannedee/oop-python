from player import get_player


class Game:
    counter = 0

    def __init__(self, num_players=2, target_score=100):
        self.target_score = target_score
        self.players = [get_player(i + 1) for i in range(num_players)]
        Game.counter += 1
        self.num = Game.counter

    def run(self):
        self._start()
        self._play()
        self._end()

    def _start(self):
        print(f'--- {self} START ---')

    def _end(self):
        print(f'--- {self} END ---')

    def _play(self):
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
        hi_score_player = None
        hi_score = 0

        for player in self.players:
            if player.score > hi_score:
                hi_score_player = player
                hi_score = player.score
        return hi_score_player

    def __str__(self):
        return f'Game {self.num}'
