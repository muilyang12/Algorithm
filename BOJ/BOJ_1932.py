def maximize_sum(num, data):
    if num == 1:
        print(data[0][0])
        return
    
    memo = data.copy()

    for i in range(num - 1, 0, -1):
        for j in range(i):
            memo[i][j] = max(memo[i][j] + memo[i + 1][j], memo[i][j] + memo[i + 1][j + 1])

    print(memo[1][0])



num = int(input())
data = [[]]
for i in range(1, num + 1):
    data.append(input().strip().split())

    for j in range(i):
        data[i][j] = int(data[i][j])

maximize_sum(num, data)