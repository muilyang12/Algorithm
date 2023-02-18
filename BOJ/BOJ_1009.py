import sys
input = sys.stdin.readline

num = int(input())
data = []
for _ in range(num):
    a, b = map(int, input().split())

    if(b == 1):
        data.append(a % 10)
        continue

    a_list = []
    a_list.append(a % 10)
    count = 1

    while True:
        temp = (a_list[count - 1] * a_list[0]) % 10
        if temp == a_list[0]:
            break

        a_list.append(temp)
        count += 1

    data.append(a_list[(b % count) - 1])

for d in data:
    if d == 0:
        print(10)
        continue

    print(d)