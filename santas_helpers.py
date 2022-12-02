
def file_lines(filename, parser=None):
  with open(filename) as f:
    for line in f.readlines():
      if parser is None:
        yield line.strip()
      else:
        yield parser(line.strip())


def dict_value_to_key(d: dict, v):
  keys = list(d.keys())
  values = list(d.values())
  return keys[values.index(v)]
