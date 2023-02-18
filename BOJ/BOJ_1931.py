import sys
input = sys.stdin.readline

def set_schedule(num, reqs):
    print(reqs)
    reqs.sort(key=lambda x: (x[1], x[0]))
    print(reqs)

    first = reqs[0][1]
    last = reqs[-1][1]

    dp = [0] * (last + 1)
    dp[first] = 1
        



num = int(input())
reqs = []
for _ in range(num):
    l, r = map(int, input().split())
    reqs.append((l, r))

set_schedule(num, reqs)