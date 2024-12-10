from itertools import product

with open('input.txt', 'r') as f:
  input_data = f.readlines()

# input_data = '''190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20'''
# input_data = input_data.split('\n')

test_cases = []
for line in input_data:
  raw_output, raw_inputs = line.split(':')
  output = int(raw_output)
  inputs = [int(x) for x in raw_inputs.split()]
  test_cases.append((output, inputs))

def apply_operator(left, right, operator):
  if operator == '+':
    return left + right
  elif operator == '*':
    return left * right
  elif operator == '|':
    return int(f'{left}{right}')

calibration = 0
for test_case in test_cases:
  target = test_case[0]
  inputs = test_case[1]
  for operators in product('*+|', repeat=len(inputs)-1):
    running_target = apply_operator(inputs[0], inputs[1], operators[0])
    for i in range(1, len(operators)):
      running_target = apply_operator(running_target, inputs[i+1], operators[i])
    if target == running_target:
      calibration += target
      break

print(calibration)
# 129140 - too low (originally was combinations instead of the product)
# 465126289353
