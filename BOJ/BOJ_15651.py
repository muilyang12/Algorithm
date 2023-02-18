import sys
input = sys.stdin.readline

def print_n_m(n, m, nums, depth):
    if depth == 0:
        for _ in range(m):
            nums.append(0)

    if depth == m:
        for num in nums:
            print(num, end=" ")

        print()
        return

    for i in range(1, n + 1):
        nums[depth] = i

        print_n_m(n, m, nums, depth + 1)





n, m = map(int, input().split())
print_n_m(n, m, [], 0)
