with open('input.txt', 'r') as f:
  input_data = f.readlines()

# input_data = '''89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732'''
# input_data = input_data.split('\n')

grid = []
for line in input_data:
  grid.append([int(i) for i in line.strip()])

def calculate_rating(grid, row, col):
  found_peaks = 0
  cur_val = grid[row][col]
  if cur_val == 9:
    print(f"    Found max at {row}, {col}")
    return 1
  for test_coords in [(row, max(0, col - 1)),
                      (row, min(len(grid[0]) - 1, col + 1)),
                      (max(0, row - 1), col),
                      (min(len(grid) - 1, row +1), col )]:
    if test_coords != (row, col):
      # print(f"  Coming from {row}, {col} ({grid[row][col]}) and checking out {test_coords[0], test_coords[1]}")
      if grid[test_coords[0]][test_coords[1]] == cur_val + 1:
        found_peaks += calculate_rating(grid, test_coords[0], test_coords[1])
  return found_peaks

running_rating = 0
for row, row_data in enumerate(grid):
  for col, col_data in enumerate(row_data):
    if grid[row][col] == 0:
      print(f"Starting at {row}, {col}")
      running_rating += calculate_rating(grid, row, col)

print("hi", running_rating)