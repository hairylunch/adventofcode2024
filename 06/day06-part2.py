import copy

with open('input.txt', 'r') as f:
  input_data = f.readlines()

# test data
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
      start_row, start_col = row, col
      if col_value == '^':
        initial_heading_offsets = up
      elif col_value == 'v':
        initial_heading_offsets = down
      elif col_value == '>':
        initial_heading_offsets = right
      elif col_value == '<':
        initial_heading_offsets = left

def move_or_turn(cur_row, cur_col, heading_offsets, grid):
  try:
    # check the next location:
    # print(f"Checking out {cur_row + heading_offsets[0]}, {cur_col + heading_offsets[1]}")
    if grid[cur_row + heading_offsets[0]][cur_col + heading_offsets[1]] == '#':
      # print(f"Bumped into obstacle at {cur_row + heading_offsets[0]}, {cur_col + heading_offsets[1]} while heading was {heading_offsets}")
      # turn as we've run into something
      heading_index = directions_clockwise.index(heading_offsets)
      if heading_index == 3:
        new_heading_index = 0
      else:
        new_heading_index = heading_index + 1
      heading_offsets = directions_clockwise[new_heading_index]
      return(cur_row, cur_col, heading_offsets)
    else:
      cur_row += heading_offsets[0]
      cur_col += heading_offsets[1]
      return(cur_row, cur_col, heading_offsets)
  except IndexError: # ran off with high indices
    raise IndexError

visited_squares = {(start_row, start_col)}
distance = 0
possible_loop_count = 0

# Find the squares that are on the path
cur_row, cur_col, heading_offsets = start_row, start_col, initial_heading_offsets
while cur_row >= 0 and cur_col >= 0:
  try:
    new_row, new_col, new_heading_offsets = move_or_turn(cur_row, cur_col, heading_offsets, grid)
    if new_row == cur_row and new_col == cur_col:
      heading_offsets = new_heading_offsets
    else:
      cur_row = new_row
      cur_col = new_col
      visited_squares.add((cur_row, cur_col))
  except IndexError:  # ran off with high indices
    break

print(visited_squares)

loop_obstacles = set()
# Test adding obstacles
for test_row, test_col in visited_squares:
  if test_row >=0 and test_col >=0 and grid[test_row][test_col] != "#" and (test_row, test_col) != (start_row, start_col):
    # initial data for test run
    cur_row, cur_col, heading_offsets = start_row, start_col, initial_heading_offsets
    bumped_obstacles = set()

    test_grid = copy.deepcopy(grid)
    test_grid[test_row][test_col] = '#'
    print(f"Added obstacle to grid at {test_row, test_col}")

    while cur_row >= 0 and cur_col >= 0:
      try:
        new_row, new_col, new_heading_offsets = move_or_turn(cur_row, cur_col, heading_offsets, test_grid)
        if new_row == cur_row and new_col == cur_col:
          #print(f"  Bumped into obstacle while at {cur_row}, {cur_col} and heading {heading_offsets}")

          # Check if we're in a loop
          if (cur_row, cur_col, heading_offsets) in bumped_obstacles:
            print(f"  Found loop by adding obstacle at {test_row}, {test_col}")
            possible_loop_count += 1
            loop_obstacles.add((test_row, test_col))
            break
          else:
            bumped_obstacles.add((cur_row, cur_col, heading_offsets))

          heading_offsets = new_heading_offsets
        else:
          cur_row = new_row
          cur_col = new_col
      except IndexError: # ran off with high indices
        break

print(possible_loop_count, len(loop_obstacles))
# 1658
# 1659
# 1657