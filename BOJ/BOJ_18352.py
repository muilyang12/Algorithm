from collections import deque
import sys
input = sys.stdin.readline

# BFS
def get_cities(city, road, dist, start, cons):
    visited = [False] * (city + 1)
    shortest = [-1] * (city + 1)

    queue = deque()
    queue.append(start)
    visited[start] = True
    shortest[start] = 0

    while queue:
        now = queue.popleft()

        for next_node in cons[now]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
                shortest[next_node] = shortest[now] + 1
    
    there_is = False
    for i in range(1, city + 1):
        if shortest[i] == dist:
            print(i)
            there_is = True
    
    if not there_is:
        print(-1)



city, road, dist, start = map(int, input().split())
cons = [[] for _ in range(city + 1)]
for _ in range(road):
    fr, to = map(int, input().split())
    cons[fr].append(to)

for con in cons:
    con.sort()

get_cities(city, road, dist, start, cons)