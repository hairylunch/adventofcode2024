with open('input.txt', 'r') as f:
  input_data = f.readlines()

# test data (should get 18)
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# input_data = ['MMMSXXMASM', 'MSAMXMSMSA', 'AMXSXMAAMM', 'MSAMASMSMX', 'XMASAMXAMM', 'XXAMMXXAMA', 'SMSMSASXSS', 'SAXAMASAAA', 'MAMMMXMMMM', 'MXMXAXMASX']

grid = []
for line in input_data:
  grid.append([i for i in line.strip()])

min_row = 0
min_col = 0
max_row = len(grid)
max_col = len(grid[0])


# this implementation was finding winding/twisting ones, not just straight words
def find_adjacent_letter(grid, target_letter, row_index, col_index):
  found_count = 0
  print(f"looking for {target_letter} starting at {row_index}, {col_index}")
  target_letters = ['X', 'M', 'A', 'S']
  search_rows = range(max(min_row, row_index - 1), min(max_row, row_index + 2))
  search_cols = range(max(min_col, col_index - 1), min(max_col, col_index + 2))
  for x in search_rows:
    for y in search_cols:
      # no need to exclude self since it won't be the target value
      print(f"  Checking {x},{y} for {target_letter}, found {grid[x][y]}")
      if grid[x][y] == target_letter:
        print(f"found target letter {target_letter} at {x}, {y}, found_count is {found_count} having started at {row_index}, {col_index}")
        if target_letter == 'S':
          found_count += 1
        else:
          next_target_letter = target_letters[target_letters.index(target_letter) + 1]
          return find_adjacent_letter(grid, next_target_letter, x, y)

  print(f"Found {found_count} starting at {row_index}, {col_index}")
  return found_count

target_letters = ['X', 'M', 'A', 'S']

# walk the grid
count = 0
for row_index, row_values in enumerate(grid):
  for col_index, col_value in enumerate(row_values):
    if col_value == 'X':
      # search in the 8 directions, using row/col offsets:
      for row_offset in [-1, 0, 1]:
        for col_offset in [-1, 0, 1]:
          try:
            if (row_index + 3 * row_offset > -1 and col_index + 3 * col_offset > -1 # explict check to prevent negative indices
                and grid[row_index + row_offset][col_index + col_offset] == 'M'
                and grid[row_index + 2 * row_offset][col_index + 2 * col_offset] == 'A'
                and grid[row_index + 3 * row_offset][col_index + 3 * col_offset] == 'S'):
              # convert to 1 based indices to match text editor
              # print(f"Found one starting at {row_index+1}, {col_index+1} with offsets of {row_offset}, {col_offset} ")
              count += 1
          except IndexError:
            # print(f"ran off the grid starting at {row_index}, {col_index} with offsets of {row_offset}, {col_offset}")
            pass

print(count)
# 2633