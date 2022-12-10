'''
--- Day 10: Cathode-Ray Tube ---

1. Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?
2. Render the image given by your program. What eight capital letters appear on your CRT?
'''

from santas_helpers import file_lines

def parse_instructions(s):
  try:
    o = s.split(' ')
    return (o[0], int(o[1])) if o[0] == 'addx' else (o[0], 0)
  except:
    return None


data = []
crt = []

next_instruction_in_cycles = 0
signal_strenght_sum = 0

# Register (sprite position)
X = 1

for line in file_lines("./input_10.txt", parser=parse_instructions):
  data.append(line)

for i in range(1, 241):
  # Begin cycle
  if next_instruction_in_cycles == 0:
    # Begin executing new instruction
    instruction, value = data[0]
    data = data[1:]
    if instruction == 'addx':
      next_instruction_in_cycles = 2
    else:
      next_instruction_in_cycles = 1
  # Part 1
  if i in [20, 60, 100, 140, 180, 220]:
    signal_strenght_sum += i * X
  # Part 2
  sprite_position = (X - 1, X, X + 1)
  if len(crt) % 40 in sprite_position:
    crt.append('█')
  else:
    crt.append(' ')
  # Count down until next instruction
  next_instruction_in_cycles -= 1
  if next_instruction_in_cycles == 0:
    # End addx instruction
    if instruction == 'addx':
      X += value

print(f"Part 1: {signal_strenght_sum}")
print(f"Part 2:")
for i in range(0, len(crt), 40):
  print(''.join(crt[i:i+40]))
