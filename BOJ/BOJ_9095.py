num = int(input())
data = []
for i in range(num):
    data.append(int(input()))

for i in range(num):
    if data[i] == 1:
        print(1)
        continue

    elif data[i] == 2:
        print(2)
        continue

    elif data[i] == 3:
        print(4)
        continue

    memo = [0] * (data[i] + 1)

    memo[1] = 1
    memo[2] = 2
    memo[3] = 4

    for j in range(4, data[i] + 1):
        memo[j] = memo[j - 1] + memo[j - 2] + memo[j - 3]

    print(memo[data[i]])