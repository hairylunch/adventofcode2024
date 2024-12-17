with open('input.txt', 'r') as f:
  input_data = f.read()

# input_data = "125 17"

initial_state = [x for x in input_data.strip().split()]
print(initial_state)

test_data = initial_state.copy()

total_blinks = 25
for blink_count in range(total_blinks):
  print(test_data)
  after_blink_data = []
  for i in test_data:
    if i == '0':
      after_blink_data.append('1')
    elif len(i) % 2 == 0:
      after_blink_data.append(i[:int((len(i) / 2))])

      # avoid adding zeros/trim leading 0s
      second_value = i[int((len(i) / 2)):]
      after_blink_data.append(
        str(int(i[int((len(i) / 2)):]))
      )
    else:
      after_blink_data.append(str(int(i) * 2024))
  test_data = after_blink_data

print(len(after_blink_data))
#67 (was not stripping out zeros, loop count was only 6)
#63 (loop count was only 6)
# 103883 - too low
# 186203 - don't drop 0s