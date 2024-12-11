with open('input.txt', 'r') as f:
  input_data = f.read()

# input_data = '2333133121414131402'

disk_map = [int(x) for x in input_data.strip()]
file_number = 0
# might be a more efficient way to do this coming at it from both sides
# naive approach mimicing the write up
uncompressed = []

for i, value in enumerate(disk_map):
  if i % 2: # free space
    for i in range(value):
      uncompressed.append(None)
  else:
    for i in range(value):
      uncompressed.append(file_number)
    file_number += 1

print(uncompressed)
compressed = uncompressed.copy()

def find_start_index_of_free_space_of_size_n(n, disk_layout):
  start_index = None
  for i, value in enumerate(disk_layout):
    if start_index is None:
      if value is None:
        start_index = i
        if n == 1:
          return start_index
      else:
        continue
    else:
      if value is None:
        current_length = i - start_index + 1
        if current_length < n:
          continue
        if current_length == n:
          return start_index
      else:
        start_index = None
  return None

tracking_value = None
start_index = None
for i, value in enumerate(reversed(uncompressed)):
  if tracking_value is None:
    if value is None:
      continue
    else:
      print(f"Starting to track {value} at {i}")
      tracking_value = value
      start_index = i
      continue

  if value != tracking_value: # end of the run
    file_length = i - start_index
    print(f"Found end of {tracking_value}, index is {i}, length is {file_length}")
    insert_index = find_start_index_of_free_space_of_size_n(file_length, compressed)
    print(f"Insert index is {insert_index} for {tracking_value}")

    # modify the compressed layout
    if insert_index and insert_index < len(compressed) - i:
      for j in range(insert_index, insert_index + file_length):
        compressed[j] = tracking_value
      # "delete" the values
      for j in range(len(compressed) - i, len(compressed) - start_index):
        print(f"Deleting index {j}")
        compressed[j] = None
    tracking_value = value
    if tracking_value is None:
      start_index = None
    else:
      start_index = i

print(compressed)

checksum = 0
for i, value in enumerate(compressed):
  if value is not None:
    checksum += i * int(value)

print(checksum)
