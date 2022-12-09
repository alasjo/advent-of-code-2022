'''
Helper functions for AoC solutions
'''

import math


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


def print_positions(pos: set):
  x_min = 0
  x_max = 0
  y_min = 0
  y_max = 0
  for xx, yy in pos:
    if xx > x_max:
      x_max = xx
    if xx < x_min:
      x_min = xx
    if yy > y_max:
      y_max = yy
    if yy < y_min:
      y_min = yy
  for y in range(y_min, y_max + 1):
    for x in range(x_min, x_max + 1):
      o = "#" if (x, y) in pos else "."
      print(o, end="")
    print()


def taxi_distance(x_1, y_1, x_2, y_2):
  return abs(x_2 - x_1) + abs(y_2 - y_1)


def two_d_euclidean_distance(x_1, y_1, x_2, y_2):
  return math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))


two_axis_directions = {
  'U': (0, -1), # UP
  'R': (1, 0),  # RIGHT
  'D': (0, 1),  # DOWN
  'L': (-1, 0), # LEFT
}
