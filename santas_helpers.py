'''
Helper functions for AoC solutions
'''

# Read file lines, optionally parse them
def file_lines(filename, parser=None, trim=True):
  with open(filename) as f:
    for line in f.readlines():
      if parser is None:
        yield line.strip() if trim else line
      else:
        yield parser(line.strip() if trim else line)


# Return a dict key corresponding to a value
def dict_value_to_key(d: dict, v):
  keys = list(d.keys())
  values = list(d.values())
  return keys[values.index(v)]


# Intersect two iterables, returning a new list of the common elements
def list_intersect(l, m):
  return [e for e in list(l) if e in list(m)]


def multiply_list(l: list):
  result = 1
  for e in l:
    result *= e
  return result


two_axis_directions = {
  'U': (0, -1), # UP
  'R': (1, 0),  # RIGHT
  'D': (0, 1),  # DOWN
  'L': (-1, 0), # LEFT
}
