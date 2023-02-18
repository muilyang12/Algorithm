num = int(input())
data = []
for _ in range(num):
    name, k, e, m = input().strip().split()
    data.append((name, int(k), int(e), int(m)))

data.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in data:
    print(student[0])