with open('input.txt', 'r') as f:
  input_data = f.readlines()

# test data (should get 18)
# input_data = '''....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...'''
# input_data = input_data.split('\n')


grid = []
for line in input_data:
  grid.append([i for i in line.strip()])

cur_col = 0
cur_row = 0
# Offsets for row and col based upon heading
up = (-1, 0)
down = (1,0)
left = (0, -1)
right = (0, 1)

directions_clockwise = [up, right, down, left]

for row, row_values in enumerate(grid):
  for col, col_value in enumerate(row_values):
    if col_value in ['^', 'v', '>', '<']:
      cur_row, cur_col = row, col
      if col_value == '^':
        heading_offsets = up
      elif col_value == 'v':
        heading_offsets = down
      elif col_value == '>':
        heading_offsets = right
      elif col_value == '<':
        heading_offsets = left

visited_squares = {(cur_row, cur_col)}
while cur_row >= 0 and cur_col >= 0:
  try:
    # check the next location:
    print(f"Checking out {cur_row + heading_offsets[0]}, {cur_col + heading_offsets[1]}")
    if grid[cur_row + heading_offsets[0]][cur_col + heading_offsets[1]] == '#':
      # turn as we've run into something
      heading_index = directions_clockwise.index(heading_offsets)
      if heading_index == 3:
        new_heading_index = 0
      else:
        new_heading_index = heading_index + 1
      heading_offsets = directions_clockwise[new_heading_index]
    else:
      cur_row += heading_offsets[0]
      cur_col += heading_offsets[1]
      visited_squares.add((cur_row, cur_col))
  except IndexError: # ran off with high indicies
    print(len(visited_squares))
    exit()

# fallback for if you ran off with low indices
# subtracting one since we can't visit the negative index
print(len(visited_squares)-1)

