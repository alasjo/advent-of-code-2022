'''
--- Day 8: Treetop Tree House ---

1. Consider your map; how many trees are visible from outside the grid?
2. Consider each tree on your map. What is the highest scenic score possible for any tree?
'''

from santas_helpers import file_lines, multiply_list, two_axis_directions

def parse_trees(s):
  try:
    return [int(c) for c in s]
  except:
    return None


# Part 1, generator to deduce duplicates
def determine_visible(d, x, y, dx, dy):
  t = data[y][x]
  while True:
    # Peek ahead
    nx, ny = (x + dx, y + dy)
    if nx < 1 or nx >= len(d[0]) - 1:
      break
    if ny < 1 or ny >= len(d) - 1:
      break
    # Next visible?
    if d[ny][nx] > t:
      # Add and step
      # print((nx, ny), "visible:", d[ny][nx])
      yield((nx, ny))
      x, y = (nx, ny)
      t = d[y][x]
    else:
      x, y = (nx, ny)


# Part 2, get view distance from point
def viewing_distance(d, x, y, dx, dy):
  t = data[y][x]
  n = 0 # viewing distance
  while True:
    # Peek ahead
    nx, ny = (x + dx, y + dy)
    if nx < 0 or nx > len(d[0]) - 1:
      break
    if ny < 0 or ny > len(d) - 1:
      break
    n += 1
    # View obstructed?
    if d[ny][nx] >= t:
      break
    else:
      # Step further
      x, y = (nx, ny)
  return n


data = []
directions = two_axis_directions.copy()

for line in file_lines("./input_8.txt", parser=parse_trees):
  data.append(line)

'''
Part 1
'''

# Count trees visible on the edge
visible = len(data) * 2 + (len(data[0]) - 2) * 2
# Set to hold interior trees (visible)
interior_trees_visible = set()

# From the top, down
for x in range(1, len(data[0]) - 1):
  y = 0
  dx, dy = directions['D']
  for t in determine_visible(data, x, y, dx, dy):
    interior_trees_visible.add(t)

# From the bottom, up
for x in range(1, len(data[0]) - 1):
  y = len(data) - 1
  dx, dy = directions['U']
  for t in determine_visible(data, x, y, dx, dy):
    interior_trees_visible.add(t)

# From the left, right
for y in range(1, len(data) - 1):
  x = 0
  dx, dy = directions['R']
  for t in determine_visible(data, x, y, dx, dy):
    interior_trees_visible.add(t)

# From the right, left
for y in range(1, len(data) - 1):
  x = len(data[0]) - 1
  dx, dy = directions['L']
  for t in determine_visible(data, x, y, dx, dy):
    interior_trees_visible.add(t)

'''
Part 2
'''

scenic_score_max = 0

for y in range(len(data)):
  for x in range(len(data[0])):
    tree_viewing_distances = {}
    for d in directions.keys():
      dx, dy = directions[d]
      tree_viewing_distances[d] = viewing_distance(data, x, y, dx, dy)
    scenic_score = multiply_list(tree_viewing_distances.values())
    if scenic_score > scenic_score_max:
      scenic_score_max = scenic_score

'''
Output
'''

visible += len(interior_trees_visible)

print(f"Part 1: {visible}")
print(f"Part 2: {scenic_score_max}")
