'''
--- Day 1: Calorie Counting ---

1. Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
2. Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
'''

from santas_helpers import file_lines

def parse_calories(s):
  try:
    return int(s, 10)
  except:
    return '---'


elves = [0]

for line in file_lines("./input_1.txt", parser=parse_calories):
  if type(line) == int:
    elves[-1] += line
  else:
    elves.append(0)

elves.sort(reverse=True)

print(f"Part 1: {elves[0]}")
print(f"Part 2: {sum(elves[:3])}")
