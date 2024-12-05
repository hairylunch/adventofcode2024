from collections import defaultdict

with open('input.txt', 'r') as f:
  input_data = f.read()

# input_data = '''47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13
#
# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47'''

raw_rules, raw_input = input_data.split("\n\n")

# dictionary that has number as the key and value is list of page that have to come before it
rules = defaultdict(list)
for rule in raw_rules.split("\n"):
  before, after = rule.split('|')
  rules[int(after)].append(int(before))

# reverse the updates lists
updates = []
for i in raw_input.split("\n"):
  if i:
    updates.append([int(j) for j in i.split(',')][::-1])

output = 0

for update in updates:
  valid_order = True
  for i, value in enumerate(update, 1):
    for previous_value in update[i:]:
      if value in rules[previous_value]:
        valid_order = False
        break
  if valid_order:
    output += update[int(len(update)/2)]

print(output)
