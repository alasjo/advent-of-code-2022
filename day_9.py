'''
--- Day 9: Rope Bridge ---

1. Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?
2. Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of the rope visit at least once?
'''

from santas_helpers import file_lines, two_axis_directions, two_d_euclidean_distance

def parse_motions(s):
  try:
    a, b = s.split(' ')
    return (a, int(b))
  except:
    return None


# Visited positions
positions_part_1 = set()
positions_part_2 = set()

# Knots
knots = [(0,0) for _ in range(10)]

for line in file_lines("./input_9.txt", parser=parse_motions):
  step, count = line
  dx, dy = two_axis_directions[step]
  for i in range(count):
    # Move the head
    knots[0] = (knots[0][0] + dx, knots[0][1] + dy)
    for i in range(1, len(knots)):
      # Set the "head"
      hx, hy = knots[i - 1]
      # Current knot
      tx, ty = knots[i]
      # Determine distance
      distance = round(two_d_euclidean_distance(hx, hy, tx, ty))
      if distance > 1.0:
        # Need to move tail
        if hx == tx:
          # Same column
          ty = ty + 1 if hy > ty else ty - 1
        elif hy == ty:
          # Same row
          tx = tx + 1 if hx > tx else tx - 1
        elif distance >= 2.0:
          # Diagonal
          tx = tx + 1 if hx > tx else tx - 1
          ty = ty + 1 if hy > ty else ty - 1
      # Set position of current knot
      knots[i] = (tx, ty)
    # Add current positions
    positions_part_1.add(knots[1])
    positions_part_2.add(knots[-1])

print(f"Part 1: {len(positions_part_1)}")
print(f"Part 2: {len(positions_part_2)}")
