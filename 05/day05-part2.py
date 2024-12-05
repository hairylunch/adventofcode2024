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

def is_order_valid(input_list, rules):
  for i, value in enumerate(input_list, 1):
    for previous_value in input_list[i:]:
      if value in rules[previous_value]:
        return False
  return True

# returns the indices of the number and the one that should come after
def find_out_of_order_number(input_list, rules):
  for i, value in enumerate(input_list):
    for previous_value in input_list[i+1:]:
      if value in rules[previous_value]:
        return(i, input_list.index(previous_value))

def reorder_and_get_middle_value(input_list, rules):
  print(f"Trying to reorder {input_list}")
  if is_order_valid(input_list, rules):
    value = input_list[int(len(input_list)/2)]
    print(f"returning {value}")
    return value
  else:
    i, j = find_out_of_order_number(input_list, rules)
    input_list[i], input_list[j] = input_list[j], input_list[i]
    return reorder_and_get_middle_value(input_list, rules)

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
  if not is_order_valid(update, rules):
    value = reorder_and_get_middle_value(update, rules)
    print(value)
    output += value

print(output)
