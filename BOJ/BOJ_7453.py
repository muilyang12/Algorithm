num = int(input())

a, b, c, d = [], [], [], []
for i in range(num):
    aaa, bbb, ccc, ddd = map(int, input().split())

    a.append(aaa)
    b.append(bbb)
    c.append(ccc)
    d.append(ddd)

ab = {}
for aaa in a:
    for bbb in b:
        if not ab.get(aaa + bbb):
            ab[aaa + bbb] = 1

        else:
            ab[aaa + bbb] += 1

cd = {}
for ccc in c:
    for ddd in d:
        if not cd.get(ccc + ddd):
            cd[ccc + ddd] = 1

        else:
            cd[ccc + ddd] += 1

count = 0

for i in ab.keys():
    if -i in cd.keys():
        count += ab[i] * cd[-i]

print(count)



# def make_zero(data):
#     temp_one = []
#     for i in range(num):
#         for j in range(num):
#             temp_one.append(data[0][i] + data[1][j])

#     temp_two = []
#     temp_two_dict = {}
#     for i in range(num):
#         for j in range(num):
#             if not temp_two_dict.get(data[2][i] + data[3][j]):
#                 temp_two.append(data[2][i] + data[3][j])
#                 temp_two_dict[data[2][i] + data[3][j]] = 1

#             else:
#                 temp_two_dict[data[2][i] + data[3][j]] += 1

#     temp_two.sort()

#     count = 0

#     for t in temp_one:
#         left = 0
#         right = len(temp_two) - 1

#         while left <= right:
#             mid = (left + right) // 2

#             if temp_two[mid] == -t:
#                 count += temp_two_dict[temp_two[mid]]
#                 break

#             elif temp_two[mid] < -t:
#                 left = mid + 1
#                 right = right

#             elif temp_two[mid] > -t:
#                 left = left
#                 right = mid - 1

#     print(count)


# num = int(input())

# data = [[], [], [], []]
# for i in range(num):
#     a, b, c, d = map(int, input().split())

#     data[0].append(a)
#     data[1].append(b)
#     data[2].append(c)
#     data[3].append(d)

# make_zero(data)