from player import Player


class Game:
    counter = 0

    def __init__(self, num_players=2, target_score=100):
        self.players = [Player(i + 1) for i in range(num_players)]
        self.target_score = target_score
        Game.counter += 1
        self.num = Game.counter

    def run(self):
        self._start_display()
        self._take_turns()
        self._end_display()

    def _take_turns(self):
        while True:
            for player in self.players:
                player.take_turn()

            if self.is_over():
                winner = self.winner
                print(f'{winner} wins!')
                return

    def is_over(self):
        for player in self.players:
            if player.score >= self.target_score:
                return True
        return False

    @property
    def winner(self):
        max_score = 0
        cur_winner = None
        for player in self.players:
            if player.score > max_score:
                cur_winner = player
                max_score = player.score
        return cur_winner

    def _start_display(self):
        print(f"--- START {self} ---".upper())

    def _end_display(self):
        print(f"--- END {self} ---".upper())

    def __str__(self):
        return f'Game {self.num}'
