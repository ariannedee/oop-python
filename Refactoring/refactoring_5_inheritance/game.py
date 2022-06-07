from player import get_player


class Game:
    counter = 0

    def __init__(self, num_players=2, target_score=100):
        self.target_score = target_score
        self.players = [get_player(i + 1) for i in range(num_players)]
        Game.counter += 1
        self.num = Game.counter

    def run(self):
        print(f'-- {self} start --')
        while True:
            for player in self.players:
                player.make_move()
            if self.is_over():
                print(f'{self.winner} wins!')
                break
        print(f'-- {self} end --')

    def is_over(self):
        for player in self.players:
            if player.score >= self.target_score:
                return True

    @property
    def winner(self):
        if not self.is_over():
            return None
        max_score = 0
        winner = None
        for player in self.players:
            if player.score > max_score:
                max_score = player.score
                winner = player
        return winner

    def __str__(self):
        return f'Game {self.num}'

    def __repr__(self):
        return f'Game({len(self.players)})'
