'''
Helper functions for AoC solutions
'''

# Read file lines, optionally parse them
def file_lines(filename, parser=None):
  with open(filename) as f:
    for line in f.readlines():
      if parser is None:
        yield line.strip()
      else:
        yield parser(line.strip())


# Return a dict key corresponding to a value
def dict_value_to_key(d: dict, v):
  keys = list(d.keys())
  values = list(d.values())
  return keys[values.index(v)]


# Intersect two iterables, returning a new list of the common elements
def list_intersect(l, m):
  return [e for e in list(l) if e in list(m)]
