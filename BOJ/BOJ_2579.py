def step(num, data):
    if num == 1:
        print(data[1])
        return

    if num == 2:
        print(data[1] + data[2])
        return

    if num == 3:
        print(max(data[1] + data[3], data[2] + data[3]))
        return

    memo = [0] * (num + 1)
    memo[1] = data[1]
    memo[2] = data[1] + data[2]
    memo[3] = max(data[1] + data[3], data[2] + data[3])

    for i in range(4, num + 1):
        memo[i] = max(memo[i - 2] + data[i], memo[i - 3] + data[i - 1] + data[i])

    print(memo[num])

num = int(input())
data = [0]
for i in range(num):
    data.append(int(input()))

step(num, data)