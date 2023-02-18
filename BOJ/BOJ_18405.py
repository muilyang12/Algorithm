from collections import deque
import sys
input = sys.stdin.readline

def get_virus(n, k, s, x, y, graph):
    time_arr = [[-1 for _ in range(n)] for _ in range(n)]
    
    queue = deque()

    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                time = 0

                queue.append((i, j, graph[i][j], time))
                time_arr[i][j] = time

    direc_x = [-1, 1, 0, 0]
    direc_y = [0, 0, -1, 1]

    while queue:
        now_x, now_y, value, time = queue.popleft()

        for i in range(4):
            next_x = now_x + direc_x[i]
            next_y = now_y + direc_y[i]

            if next_x > n - 1 or next_x < 0 or next_y > n - 1 or next_y < 0:
                continue

            if time_arr[next_x][next_y] < time + 1 and time_arr[next_x][next_y] != -1:
                continue

            if graph[next_x][next_y] < value and graph[next_x][next_y] != 0:
                continue

            if time + 1 > s:
                continue

            graph[next_x][next_y] = value
            time_arr[next_x][next_y] = time + 1
            queue.append((next_x, next_y, value, time + 1))

    print(graph[x - 1][y - 1])



n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
s, x, y = map(int, input().split())

get_virus(n, k, s, x, y, graph)