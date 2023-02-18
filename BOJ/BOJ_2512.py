import time

def get_limit(requests, total):
    requests.sort()

    left = 0
    right = requests[-1]

    result = 0

    while left <= right:
        mid = (right + left) // 2

        request_sum = 0
        for request in requests:
            request_sum = request_sum + (request if request <= mid else mid)

        if request_sum <= total:
            left = mid + 1
            right = right

            result = mid
        
        elif request_sum > total:
            left = left
            right = mid - 1

    print(result)



num = int(input())
requests = list(map(int, input().split()))
total = int(input())

get_limit(requests, total)