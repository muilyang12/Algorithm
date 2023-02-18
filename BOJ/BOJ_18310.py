import sys
input = sys.stdin.readline

def get_sum(locs, target):
    result = 0

    for loc in locs:
        result += (loc - locs[target]) if loc >= locs[target] else (locs[target] - loc)

    return result

def get_proper_loc(num, locs):
    locs.sort()

    if num == 1:
        print(0)
        return
    
    elif num == 2:
        print(locs[1] - locs[0])
        return

    target = num // 2

    left = get_sum(locs, target - 1)
    mid = get_sum(locs, target)
    right = get_sum(locs, target + 1)

    if mid < left and mid <= right:
        print(target)
        return
    
    if left <= mid:
        for l in range(target - 2, -1, -1):
            temp = get_sum(locs, l)

            if temp < left:
                left = temp
                continue

            print(locs[l + 1])
            return


    if right < mid:
        for r in range(target + 2, num, 1):
            temp = get_sum(locs, r)

            if temp < right:
                right = temp
                continue

            print(locs[r - 1])
            return



num = int(input())
locs = list(map(int, input().split()))

get_proper_loc(num, locs)