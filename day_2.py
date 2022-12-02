'''
--- Day 2: Rock Paper Scissors ---

1. What would your total score be if everything goes exactly according to your strategy guide?
2. Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
'''

from santas_helpers import file_lines, dict_value_to_key

rps_winner = {
  'R': 'S',
  'P': 'R',
  'S': 'P'
}

rps_score_table = {
  'R': 1, 'P': 2, 'S': 3,
  'W': 6, 'L': 0, 'D': 3
}


def rps_score(elf_a, elf_b):
  # Score for participating (chosen play)
  s = rps_score_table[elf_b]

  if elf_a == elf_b:
    # DRAW
    return rps_score_table['D'] + s
  
  if rps_winner[elf_a] == elf_b:
    # LOSE
    return rps_score_table['L'] + s

  if rps_winner[elf_b] == elf_a:
    # WIN
    return rps_score_table['W'] + s

  # hmm
  exit(1)


score_strategy_a = 0
score_strategy_b = 0

for line in file_lines("./input_2.txt"):
  # Strategy A
  line = line.replace('A', 'R').replace('X', 'R')
  line = line.replace('B', 'P').replace('Y', 'P')
  line = line.replace('C', 'S').replace('Z', 'S')
  elf_a, elf_b = line.split(' ')
  score_strategy_a += rps_score(elf_a, elf_b)

  # Strategy B
  if elf_b == 'R':
    # LOSE
    score_strategy_b += rps_score(elf_a, rps_winner[elf_a])
  elif elf_b == 'P':
    # DRAW
    score_strategy_b += rps_score(elf_a, elf_a)
  elif elf_b == 'S':
    # WIN
    win = dict_value_to_key(rps_winner, elf_a)
    score_strategy_b += rps_score(elf_a, win)

print(f"Part 1: {score_strategy_a}")
print(f"Part 2: {score_strategy_b}")
