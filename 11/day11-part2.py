from functools import cache

with open('input.txt', 'r') as f:
  input_data = f.read()

initial_state = [x for x in input_data.strip().split()]

@cache
def blink_single_value(value, blink_count):
  if blink_count == 0:
    return 1
  else:
    if value == '0':
      return blink_single_value('1', blink_count-1)
    elif len(value) % 2 == 0:
      # first half
      first_half = value[:int((len(value) / 2))]
      # second half, no leading zeros
      second_half = str(int(value[int((len(value) / 2)):]))
      return blink_single_value(first_half, blink_count-1) + blink_single_value(second_half, blink_count-1)
    else:
      return blink_single_value(str(int(value) * 2024), blink_count-1)

@cache
def blink(data_string, blink_count):
  parsed_values = [x for x in data_string.split()]
  stone_count = 0
  for i in parsed_values:
    stone_count += blink_single_value(i, blink_count)
  return stone_count

total_blinks = 75
value_count = 0
test_data = input_data
# test_data = '125 17'

stones_at_end = blink(test_data, total_blinks)

print(stones_at_end)
# print("made it", len(stones_at_end.split()) )


