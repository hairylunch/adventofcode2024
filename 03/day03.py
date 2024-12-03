import re

with open('input.txt', 'r') as f:
  input_data = f.read()

mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

total = 0
for i in re.finditer(mul_pattern, input_data):
  sum += int(i.group(1)) * int(i.group(2))

print(total)