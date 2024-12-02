with open('input.txt', 'r') as f:
  input_data = f.readlines()

safe = 0
for line in input_data:
  level_values = [int(i) for i in line.strip().split()]
  deltas = []
  for i in range(len(level_values) - 1):
    deltas.append(level_values[i+1] - level_values[i])
  # no need to check for delta == 0 since the all() expressions will handle that
  if max(deltas) < 4 and min(deltas) > -4 and (all(x > 0 for x in deltas) or all(x < 0 for x in deltas)):
    safe +=1

print(safe)


