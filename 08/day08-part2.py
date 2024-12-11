from collections import defaultdict
from itertools import combinations

with open('input.txt', 'r') as f:
  input_data = f.readlines()

# input_data = '''............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............'''
# input_data = input_data.split('\n')

antennas = defaultdict(list)
col_width = None
row_height = len(input_data)
for row, line in enumerate(input_data):
  col_width = len(line.strip())
  for col, value in enumerate(line):
    if value != '.':
      antennas[value].append((row, col))

count = 0
antinodes = set()
for antenna, locations in antennas.items():
  print(antenna, locations)
  for i in combinations(locations, 2):
    first_point = i[0]
    second_point = i[1]

    row_delta = first_point[0] - second_point[0]
    col_delta = first_point[1] - second_point[1]

    for direction in [1, -1]:
      potential_row = first_point[0]
      potential_col = first_point[1]
      while 0 <= potential_row < row_height and 0 <= potential_col < col_width:
        antinodes.add((potential_row, potential_col))
        potential_row += direction * row_delta
        potential_col += direction * col_delta

print(len(antinodes))
