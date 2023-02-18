def maximize_revenue(data):
    memo = [-1] * (num + 1)

    d = 0
    for d in range(num, 0, -1):
        if d + data[d][0] - 1 <= num:
            memo[d] = data[d][1]
            break

        else:
            memo[d] = 0

    if d == 1:
        print(memo[1])
        return

    for i in range(d - 1, 0, -1):
        if i + data[i][0] - 1 > num:
            memo[i] = memo[i + 1]
            continue

        if i + data[i][0] - 1 == num:
            memo[i] = max(memo[i + 1], data[i][1])
            continue

        memo[i] = max(memo[i + data[i][0]] + data[i][1], memo[i + 1])

    print(memo[1])



num = int(input())
data = [0]
for i in range(num):
    t, p = input().strip().split()
    data.append([int(t), int(p)]) 

maximize_revenue(data)