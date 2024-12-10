import copy

with open('input.txt', 'r') as f:
  input_data = f.readlines()

# test data
input_data = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''
input_data = input_data.split('\n')

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

def find_distance_to_next_obstacle(cur_row, cur_col, heading_offsets, grid):
  distance = 0
  if heading_offsets[0]:
    new_row = cur_row
    while 0 <= new_row <= len(grid):
      new_row += heading_offsets[0]
      if grid[new_row][cur_col] != '#':
        distance += 1
      else:
        break
  else:
    new_col = cur_col
    while 0 <= new_col <= len(grid[0]):
      new_col += heading_offsets[1]
      if grid[cur_row][new_col] != '#':
        distance += 1
      else:
        break
  return distance

def can_we_trap_ourselves(cur_row, cur_col, heading_offsets, grid):
  max_distance = find_distance_to_next_obstacle(cur_row, cur_col, heading_offsets, grid)
  for i in range(1, max_distance + 1) :
    test_obstacle_row = cur_row + i * heading_offsets[0]
    test_obstacle_col = cur_col + i * heading_offsets[1]
    print(
      f"  Can we trap starting at {cur_row}, {cur_col} while heading is {heading_offsets}, adding obstacle at {test_obstacle_row}, {test_obstacle_col}")
    if 0 <= test_obstacle_row <= len(grid) and 0 <= test_obstacle_col <= len(grid[0]):
      test_grid = copy.deepcopy(grid)
      test_grid[test_obstacle_row][test_obstacle_col] = '#'
      test_run_row = cur_row
      test_run_col = cur_col
      test_run_heading_offsets = heading_offsets
      obstacles = 0
      while test_run_row >= 0 and test_run_col >= 0:
        try:
          new_test_run_row, new_test_run_col, new_heading_offsets = move_or_turn(test_run_row, test_run_col, test_run_heading_offsets, test_grid)
          if new_test_run_row == test_run_row and new_test_run_col == test_run_col:
            test_run_heading_offsets = new_heading_offsets
            obstacles += 1
            if obstacles == 4:
              if new_test_run_row == cur_row and new_test_run_col == cur_col:
                print(
                  f"Found loop starting at {cur_row}, {cur_col} while heading was {heading_offsets} and adding obstacle at {test_obstacle_row}, {test_obstacle_col}")
                return True
              break
          else:
            test_run_row = new_test_run_row
            test_run_col = new_test_run_col
        except IndexError:  # ran off with high indices
          break


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


visited_squares = {(cur_row, cur_col)}
distance = 0
possible_loop_count = 0
while cur_row >= 0 and cur_col >= 0:
  try:
    new_row, new_col, new_heading_offsets = move_or_turn(cur_row, cur_col, heading_offsets, grid)
    if new_row == cur_row and new_col == cur_col:
      print(f"Bumped into obstacle while at {cur_row}, {cur_col} and heading {heading_offsets}")
      heading_offsets = new_heading_offsets
      if can_we_trap_ourselves(cur_row, cur_col, heading_offsets, grid):
        possible_loop_count += 1
    else:
      cur_row = new_row
      cur_col = new_col
      visited_squares.add((cur_row, cur_col))
      distance +=1
  except IndexError: # ran off with high indices
    break

print(possible_loop_count)
# 102 too low