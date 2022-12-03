'''
--- Day 3: Rucksack Reorganization ---

1. Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
2. Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?
'''

from santas_helpers import file_lines, list_intersect
from string import ascii_letters


def parse_rucksack(s):
  try:
    l = len(s) // 2
    # Return rucksack compartments
    return (s[:l], s[l:], s)
  except:
    print("nope")


def translate_item(c):
  return ascii_letters.index(c) + 1


data = []
priority_sum_1 = 0
priority_sum_2 = 0

for line in file_lines("./input_3.txt", parser=parse_rucksack):
  data.append(line)

for r in data:
  # Exactly one item type should be present in both compartments
  i = list_intersect(r[0], r[1])
  priority_sum_1 += translate_item(i[0])

# Groups of three elves
for i in range(0, len(data), 3):
  r, s, t = data[i:i+3]
  inter_rs = list_intersect(r[2], s[2])
  badge = list_intersect(inter_rs, t[2])[0]
  priority_sum_2 += translate_item(badge)

print(f"Part 1: {priority_sum_1}")
print(f"Part 2: {priority_sum_2}")
