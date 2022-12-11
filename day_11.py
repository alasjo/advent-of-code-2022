'''
--- Day 11: Monkey in the Middle ---

1. Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
2. Worry levels are no longer divided by three after each item is inspected; you'll need to find another way to keep your worry levels manageable. Starting again from the initial state in your puzzle input, what is the level of monkey business after 10000 rounds?
'''

from santas_helpers import file_lines, multiply_list, gcd
import re


class Monkey:
  def __init__(self, items, operation, divisible, target_if_true, target_if_false):
    self.items = items
    self.operation = operation
    self.divisible = divisible
    self.target_if_true = target_if_true
    self.target_if_false = target_if_false
    self.inspected_count = 0

  def inspect(self, item_index = 0, divide=0, modulo=0):
    if self.has_items():
      # Monkey inspects an item
      old = self.items[item_index]
      new = eval(self.operation)
      if divide > 0:
        new = new // divide
      if modulo > 0:
        new = new % modulo
      self.items[item_index] = new
      self.inspected_count += 1
    else:
      raise Exception("huh?")

  def test(self, item_index = 0):
    return self.items[item_index] % self.divisible == 0

  def throw(self):
    if self.has_items():
      item = self.items[0]
      test = self.test()
      self.items = self.items[1:]
      target = self.target_if_true if test else self.target_if_false
      return (item, target)
    else:
      raise Exception("nope")

  def give(self, item):
    self.items.append(item)

  def has_items(self):
    return len(self.items) > 0


monkeys_part_1 = []
monkeys_part_2 = []
items_pattern = re.compile(r"Starting items: ([0-9, ]+)")
operation_pattern = re.compile(r"Operation: ([new= old*+0-9]+)")
test_pattern = re.compile(r"Test: divisible by ([0-9]+)")
true_pattern = re.compile(r"If true: throw to monkey ([0-9]+)")
false_pattern = re.compile(r"If false: throw to monkey ([0-9]+)")
monkey_modulo = 1

for line in file_lines("./input_11.txt"):
  items_match = items_pattern.match(line)
  if items_match:
    items = [int(n) for n in items_match.group(1).split(", ")]
    continue
  operation_match = operation_pattern.match(line)
  if operation_match:
    operation = operation_match.group(1).split(" = ")[1]
    continue
  test_match = test_pattern.match(line)
  if test_match:
    test = int(test_match.group(1))
    continue
  true_match = true_pattern.match(line)
  if true_match:
    true_target = int(true_match.group(1))
    continue
  false_match = false_pattern.match(line)
  if false_match:
    false_target = int(false_match.group(1))
    # End of monkey section
    monkey_1 = Monkey(items[:], operation, test, true_target, false_target)
    monkey_2 = Monkey(items[:], operation, test, true_target, false_target)
    monkeys_part_1.append(monkey_1)
    monkeys_part_2.append(monkey_2)
    monkey_modulo = monkey_modulo * test

'''
Part 1
'''

for round in range(20):
  for monkey_index in range(len(monkeys_part_1)):
    # print(f"Monkey {monkey_index}")
    while monkeys_part_1[monkey_index].has_items():
      monkeys_part_1[monkey_index].inspect(divide=3)
      item, target = monkeys_part_1[monkey_index].throw()
      monkeys_part_1[target].give(item)

inspections_part_1 = sorted([m.inspected_count for m in monkeys_part_1], reverse=True)
print(f"Part 1: {multiply_list(inspections_part_1[:2])}")

'''
Part 2: completes in ~5s
'''

for round in range(10000):
  for monkey_index in range(len(monkeys_part_2)):
    while monkeys_part_2[monkey_index].has_items():
      monkeys_part_2[monkey_index].inspect(modulo=monkey_modulo)
      item, target = monkeys_part_2[monkey_index].throw()
      monkeys_part_2[target].give(item)

inspections_part_2 = sorted([m.inspected_count for m in monkeys_part_2], reverse=True)
print(f"Part 2: {multiply_list(inspections_part_2[:2])}")
