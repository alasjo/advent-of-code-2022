'''
--- Day 5: Supply Stacks ---

1. After the rearrangement procedure completes, what crate ends up on top of each stack?
2. After the rearrangement procedure completes, what crate ends up on top of each stack?
'''

from santas_helpers import file_lines
from copy import deepcopy
import re


crate_pattern = re.compile(r"\[([A-Z])\]")
move_pattern = re.compile(r"move ([0-9]+) from ([0-9]) to ([0-9])")

data_part_1 = {}
moves = []

for line in file_lines("./input_5.txt", trim=False):
  move_match = move_pattern.match(line)
  if move_match:
    moves.append([int(a) for a in move_match.groups()])
  elif '[' in line:
    # Setup stacks
    for i in range(0, len(line), 4):
      crate_index = (i // 4) + 1
      crate = crate_pattern.match(line[i:i+4])
      if crate:
        if crate_index in data_part_1:
          data_part_1[crate_index].append(crate.group(1))
        else:
          data_part_1[crate_index] = [crate.group(1)]

# Copy data for part 2
data_part_2 = deepcopy(data_part_1)

# Reverse part 1 crate lists
for k in data_part_1.keys():
  data_part_1[k].reverse()

for move in moves:
  num_crates, from_crate, to_crate = move
  # Part 1, one at a time
  for i in range(num_crates):
    crate = data_part_1[from_crate].pop()
    data_part_1[to_crate].append(crate)
  # Part 2, several at a time
  crates = data_part_2[from_crate][:num_crates]
  data_part_2[from_crate] = data_part_2[from_crate][num_crates:]
  data_part_2[to_crate] = crates + data_part_2[to_crate]

print(f"Part 1: ", end='')
for k in sorted(data_part_1.keys()):
  print(data_part_1[k][len(data_part_1[k])-1], end='')
print()

print(f"Part 2: ", end='')
for k in sorted(data_part_2.keys()):
  print(data_part_2[k][0], end='')
