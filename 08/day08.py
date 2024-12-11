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
    # if 1,1 and 5,3 delta is -4 , -2
    potential_antinodes = []
    potential_antinodes.append((first_point[0] + row_delta, first_point[1] + col_delta))
    potential_antinodes.append((second_point[0] - row_delta, second_point[1] - col_delta))
    print(f"  For {antenna} with locations {first_point} and {second_point}, potential antinodes are {potential_antinodes}")
    for potential_antinode in potential_antinodes:
      if 0 <= potential_antinode[0] < row_height and 0 <= potential_antinode[1] < col_width:
        antinodes.add(potential_antinode)

print(len(antinodes))
