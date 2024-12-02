with open('input.txt', 'r') as f:
  input_data = f.readlines()

left, right = [], []
for line in input_data:
  print(line)
  l, r = line.strip().split()
  left.append(int(l))
  right.append(int(r))

left.sort()
right.sort()
distance = 0
for i in range(len(left)):
  distance += abs(left[i] - right[i])

print(distance)


