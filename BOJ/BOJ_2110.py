def get_min_dist(home, wifi, locs):
    locs.sort()

    range_from = 1
    range_to = locs[-1] - locs[0]

    result = 0

    while range_from <= range_to:
        mid = (range_to + range_from) // 2

        array = []

        count = 1
        temp = locs[0]
        array.append(locs[0])

        for i in range(1, home):
            if locs[i] - temp >= mid:
                count = count + 1
                temp = locs[i]
                array.append(locs[i])

        if count < wifi:
            range_from = range_from
            range_to = mid - 1

        elif count >= wifi:
            range_from = mid + 1
            range_to = range_to

            result = mid

    print(result)



home, wifi = map(int, input().split())

locs = []
for i in range(home):
    locs.append(int(input()))

get_min_dist(home, wifi, locs)