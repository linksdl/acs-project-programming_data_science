# Author: Daolin Sheng
# Date: 21/09/2020


def solution():
    codes = []

    pass
    return codes


solution()


from array import array
changes = [1, 1, 1, 1]
for i in range(0, 100): changes.append(changes[-1]+changes[-4])

target = 10 ** 9
total = 0
incr = 1
prev_x = 1
for x in changes:
  if target < x:
    total += incr * (target - prev_x)
    break
  else: total += incr * (x - prev_x)
  incr += 1
  prev_x = x

print(total)