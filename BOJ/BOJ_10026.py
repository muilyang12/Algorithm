import copy
from collections import deque
import sys
input = sys.stdin.readline

def how_many_area(n, graph):
    rg_graph = copy.deepcopy(graph)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    area_num = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] in ["R", "G", "B"]:
                area_num += 1

                queue.append((graph[i][j], i, j))
                graph[i][j] = str(area_num)

            while queue:
                color, x, y = queue.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    
                    if not graph[nx][ny] in ["R", "G", "B"]:
                        continue
                    
                    if graph[nx][ny] != color:
                        continue
                    
                    queue.append((graph[nx][ny], nx, ny))
                    graph[nx][ny] = str(area_num)

    rg_queue = deque()
    rg_area_num = 0
    for i in range(n):
        for j in range(n):
            if rg_graph[i][j] in ["R", "G", "B"]:
                rg_area_num += 1

                rg_queue.append((rg_graph[i][j], i, j))
                rg_graph[i][j] = str(rg_area_num)

            while rg_queue:
                color, x, y = rg_queue.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    
                    if not rg_graph[nx][ny] in ["R", "G", "B"]:
                        continue
                    
                    if (color == "R" or color == "G") and rg_graph[nx][ny] == "B":
                        continue
                    
                    if color == "B" and rg_graph[nx][ny] != "B":
                        continue
                    
                    rg_queue.append((rg_graph[nx][ny], nx, ny))
                    rg_graph[nx][ny] = str(rg_area_num)
    
    print(area_num, rg_area_num)





n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input().strip()))
how_many_area(n, graph)
