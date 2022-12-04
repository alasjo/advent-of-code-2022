'''
--- Day 4: Camp Cleanup ---

1. In how many assignment pairs does one range fully contain the other?
2. In how many assignment pairs do the ranges overlap?
'''

from santas_helpers import file_lines, list_intersect

def parse_ranges(s):
  try:
    return [[int(i) for i in r.split('-')] for r in s.split(',')]
  except:
    return None


count_part_1 = 0
count_part_2 = 0

for range_a, range_b in file_lines("./input_4.txt", parser=parse_ranges):
  a = list(range(range_a[0], range_a[1] + 1))
  b = list(range(range_b[0], range_b[1] + 1))

  # Generate a list of the common items in range a and b
  c = list_intersect(a, b)

  # If c is equal to a or b, then one range fully contains the other
  if c == a or c == b:
    count_part_1 += 1

  # If there are any elements in the range intersection, there is an overlap
  if len(c) > 0:
    count_part_2 += 1

print(f"Part 1: {count_part_1}")
print(f"Part 2: {count_part_2}")
