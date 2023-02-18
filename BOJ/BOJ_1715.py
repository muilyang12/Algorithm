import heapq
import sys
input = sys.stdin.readline

num = int(input())
q = []
for _ in range(num):
    heapq.heappush(q, int(input()))

result = 0

while len(q) > 1:
    one, two = heapq.heappop(q), heapq.heappop(q)

    temp = one + two
    result += temp
    heapq.heappush(q, temp)

print(result)

# 리스트를 통해서 구현하고 싶었는데, 자꾸 시간초과가 나온다.
# 찾아보니 리스트를 사용할 경우, 시간 복잡도가 삽입시 0(N) 삭제시 O(1).
# 힙으로 구현한 우선순위 큐를 사용할 경우, 삽입 삭제 모두 O(log N).
# 이러니까 시간초과가 출력되지.



# import sys
# input = sys.stdin.readline

# num = int(input())
# data = []
# for _ in range(num):
#     data.append(int(input()))

# result = 0

# while len(data) > 1:
#     temp = data[0] + data[1]
#     result += temp

#     if temp > data[-1]:
#         data.append(temp)

#     else :
#         for i in range(1, len(data)):
#             if data[i] > temp:
#                 data.insert(i, temp)
#                 break

#     del data[0]
#     del data[0]

# print(result)