from collections import defaultdict

with open('input.txt', 'r') as f:
  input_data = f.readlines()

left = []
right = defaultdict(int)
for line in input_data:
  l, r = line.strip().split()
  left.append(int(l))
  right[int(r)] += 1

score = 0
for i in left:
  score += i * right[i]

print(score)
