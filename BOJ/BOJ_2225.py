# 백트래킹으로 모든 경우의 수를 체크하는 방향으로 했었는데...
# DP 구나... 어쩐지 시간초과가 계속 나오더라...

import sys
input = sys.stdin.readline

count = 0
def print_how_many_case(n, k):
    global count

    dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

    for i in range(n + 1):
        dp[1][i] = 1

    for x in range(2, k + 1):
        for y in range(n + 1):
            for z in range(y + 1):
                dp[x][y] += dp[x - 1][z]

    print(dp[k][n] % 1000000000)




n, k = map(int, input().split())
print_how_many_case(n, k)





# count = 0
# def print_how_many_case(n, k, nums, depth):
#     global count

#     if depth == 0:
#         for _ in range(k):
#             nums.append(0)

#     if k == 1:
#         print(1)

#         return

#     if depth == k:
#         temp_sum = 0
#         for num in nums:
#             temp_sum += num

#         if temp_sum == n:
#             count += 1

#             return True

#         return False

#     for i in range(0, n + 1):
#         nums[depth] = i

#         is_it_done = print_how_many_case(n, k, nums, depth + 1)

#         if is_it_done:
#             break
