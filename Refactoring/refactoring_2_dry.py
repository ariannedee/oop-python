"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.
"""
import random


def play_game():
    player_scores = [0, 0]

    while True:
        for i in range(len(player_scores)):
            player_number = i + 1
            player_die = random.randint(1, 6)
            player_scores[i] += player_die
            score = player_scores[i]
            print(f'Player {player_number} score: {score}')
            if score >= 100:
                print(f'Player {player_number} wins!')
                return


if __name__ == '__main__':
    play_game()
