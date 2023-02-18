def pinary(num):
    if num == 1:
        print(1)
        return

    elif num == 2:
        print(1)
        return
    
    memo = [0] * (num + 1)
    memo[1] = 1
    memo[2] = 1

    for i in range(3, num + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    print(memo[num])

num = int(input())

pinary(num)


# 1 // 10 // 100 101 // 1000 1010 1001 // 10000 10010 10100 10001 10101 // 

# 100000 100010 100100 101000 101010 100001 100101 101001