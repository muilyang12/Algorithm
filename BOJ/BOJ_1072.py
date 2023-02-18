import math

def find_num(x, y):
    minimum = math.ceil(x / 100)

    range_from = 0
    range_to = 1000000000

    l = range_from
    r = range_to
    mid = 0

    while l <= r:
        if y / x >= 0.99:
            mid = -1
            break

        mid = (l + r) // 2

        if int(y / x * 100) < int((y + mid) / (x + mid) * 100):
            result = mid
            r = mid - 1
            l = l

        else:
            r = r
            l = mid + 1

    print(result)





x, y = map(int, input().split())
find_num(x, y)
