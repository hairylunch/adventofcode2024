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

removed_nodes = [x for x in uncompressed if x != None ]
target_length = len(removed_nodes)

uncompressed_copy = uncompressed.copy()
compressed = []
for i, value in enumerate(uncompressed):
  if i == target_length:
    break
  if value != None:
    compressed.append(value)
  else:
    end_value = None
    while not end_value:
      if uncompressed_copy[-1]:
        end_value = uncompressed_copy[-1]
      uncompressed_copy.pop()
    compressed.append(end_value)

# print(compressed)
print(target_length)
print(len(compressed))


checksum = 0
for i, value in enumerate(compressed):
  checksum += i * int(value)


print(checksum)
# 91486187825 too low (string)
# 6447164049557 too high  (switched to array)
