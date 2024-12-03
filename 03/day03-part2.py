import re

with open('input.txt', 'r') as f:
  input_data = f.read()

input_data_as_one_line = "".join(input_data)

first_split_items = input_data_as_one_line.split("don't")

do_list = [first_split_items[0]]

for i in first_split_items[1:]:
  second_split_items = i.split('do')
  if len(second_split_items) > 1:
    # could be multiple "do" in the string
    do_list.extend(second_split_items[1:])

total = 0
mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
for i in do_list:
  for j in re.finditer(mul_pattern, i):
    total += int(j.group(1)) * int(j.group(2))

print(total)
