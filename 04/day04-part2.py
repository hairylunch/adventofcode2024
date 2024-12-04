with open('input.txt', 'r') as f:
  input_data = f.readlines()

# test data (should get 9)
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

target_letters = {'M', 'S'}

# walk the grid
count = 0
for row_index, row_values in enumerate(grid):
  # skip the first and last rows
  if 0 < row_index < len(grid) - 1:
    for col_index, col_value in enumerate(row_values):
      # ignore the first and last cols
      if 0 < col_index < len(grid) - 1:
        if col_value == 'A':
          if target_letters == {grid[row_index - 1][col_index - 1], grid[row_index + 1][col_index + 1]} == {
            grid[row_index - 1][col_index + 1], grid[row_index + 1][col_index - 1]}:
            count += 1

print(count)
# 1936