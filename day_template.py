'''
--- Day X: Description ---

1. Do A
2. Do B
'''

from santas_helpers import file_lines

def parse_(s):
  try:
    return s
  except:
    return None


data = []

for line in file_lines("./input_X.txt", parser=parse_):
  data.append(line)

print(f"Part 1: {data}")
#print(f"Part 2: {data}")
