"""
Simulate a simple board game.
There are 2 players.
Each player takes turn rolling a die and moving that number of spaces.
The first person to space 100 wins.

First pass using procedural/imperative programming
"""
import random

player_1_score = 0
player_2_score = 0

print('Start game!')

while True:
    dice = random.randint(1, 6)
    player_1_score += dice
    print(f'Player 1 rolls a {dice} (score: {player_1_score})')
    
    if player_1_score >= 100:
        print('Player 1 wins!')
        break

    dice = random.randint(1, 6)
    player_2_score += dice
    print(f'Player 2 rolls a {dice} (score: {player_2_score})')

    if player_2_score >= 100:
        print('Player 2 wins!')
        break

print()
print('Final score:')
print(f'Player 1: {player_1_score}')
print(f'Player 2: {player_2_score}')
