'''
--- Day 7: No Space Left On Device ---

1. Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
2. Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?
'''

from santas_helpers import file_lines
from anytree import Node, PreOrderIter


def parse_terminal(s):
  try:
    return s.split(' ')
  except:
    return None


root = Node('ROOT', ftype='d', size=0)
nodes = []
cd = root

for line in file_lines("./input_7.txt", parser=parse_terminal):
  if line[0] == '$':
    # Command
    cmd = line[1]
    if cmd == 'cd':
      # Change current directory
      if line[2] == '/':
        # Start from root
        cd = root
      elif line[2] == '..':
        # Move out
        cd = cd.parent
      else:
        # Move in
        for node in cd.children:
          if node.name == line[2]:
            cd = node
    elif cmd == 'ls':
      # List files
      pass
  else:
    node_name = line[1]
    if line[0] == 'dir':
      # A directory residing under `cd`
      fil = Node(node_name, ftype='d', size=0, parent=cd)
    elif line[0].isnumeric():
      # File listed under `cd`
      fil = Node(node_name, ftype='f', size=int(line[0]), parent=cd)
    nodes.append(fil)

sum_part_1 = 0
used_space = sum([node.size for node in PreOrderIter(root)])
unused_space = 70000000 - used_space
needed_to_delete = 30000000 - unused_space
dir_size_to_delete = used_space

for n in nodes:
  if n.ftype == 'd':
    # Calculate size
    directory_sum = sum([node.size for node in PreOrderIter(n)])
    if directory_sum <= 100000:
      sum_part_1 += directory_sum
    if directory_sum >= needed_to_delete and directory_sum < dir_size_to_delete:
      dir_size_to_delete = directory_sum

print(f"Part 1: {sum_part_1}")
print(f"Part 2: {dir_size_to_delete}")
