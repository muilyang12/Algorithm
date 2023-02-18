def get_height(target, trees):
    biggest = -99999
    smallest = 99999
    for tree in trees:
        biggest = max(biggest, tree)
        smallest = min(smallest, tree)

    start = smallest
    end = biggest

    range_from = start
    range_to = end
    mid = 0

    result = 0

    while range_from <= range_to:
        mid = (range_from + range_to) // 2

        length = 0

        for tree in trees:
            if tree > mid:
                length = length + tree - mid

        if length >= target:
            result = mid

            range_from = mid + 1
            range_to = range_to

        elif length < target:
            range_from = range_from
            range_to = mid - 1

    print(result)



num, target = map(int, input().split())
trees = list(map(int, input().split()))

for i in range(num):
    trees[i] = int(trees[i])

get_height(target, trees)