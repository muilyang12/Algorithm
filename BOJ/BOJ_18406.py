import sys
input = sys.stdin.readline

data = input().strip()

left = data[: len(data) // 2]
left_list = list(left)

right = data[len(data) // 2 :]
right_list = list(right)

sum_l = 0
for l in left_list:
    sum_l += int(l)

sum_r = 0
for r in right_list:
    sum_r += int(r)

if sum_l == sum_r:
    print("LUCKY")
else:
    print("READY")