
def file_lines(filename, parser=None):
  with open(filename) as f:
    for line in f.readlines():
      if parser is None:
        yield line
      else:
        yield parser(line)
