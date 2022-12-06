'''
--- Day X: Description ---

1. Do A
2. Do B
'''

from santas_helpers import file_lines

data = []

for line in file_lines("./input_6.txt"):
  data.append(line)

def find_marker(s, width=4):
  for i in range(len(s)-width):
    chunk = s[i:i+width]
    if len(set(chunk)) == width:
      return (i+width, chunk)


print(f"Part 1: {find_marker(data[0])}")
print(f"Part 2: {find_marker(data[0], width=14)}")
