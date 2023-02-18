# shallow copy, deep copy 개념을 잊어버리다니.....
# 모든 분기점을 점검하고 싶은 경우에는 temp, depth
# 개념을 도입해야 합니다. n, m 문제 기억하시죠 ??

import copy

from collections import deque
import sys
input = sys.stdin.readline

direc = {}
direc[1] = [[(0, 1)], 
            [(1, 0)], 
            [(0, -1)], 
            [(-1, 0)]]
direc[2] = [[(0, 1), (0, -1)], 
            [(1, 0), (-1, 0)]]
direc[3] = [[(0, 1), (-1, 0)], 
            [(-1, 0), (0, -1)], 
            [(0, -1), (1, 0)], 
            [(1, 0), (0, 1)]]
direc[4] = [[(-1, 0), (0, 1), (1, 0)], 
            [(0, 1), (1, 0), (0, -1)], 
            [(1, 0), (0, -1), (-1, 0)], 
            [(0, -1), (-1, 0), (0, 1)]]
direc[5] = [[(0, 1), (1, 0), (0, -1), (-1, 0)]]
def cctv_check(n, m, graph):
    queue = []
    count = 1

    for i in range(n):
        for j in range(m):
            g = graph[i][j]

            if g in range(1, 6):
                queue.append((i, j, direc[g]))

    print(draw_cctv_sight(n, m, graph, queue, 0))

result = 99999
def draw_cctv_sight(n, m, graph, queue, depth):
    global result

    if depth == len(queue):
        # print()

        temp_result = 0

        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    temp_result += 1
                
                # print(graph[i][j], end=" ")

            # print()

        result = min(result, temp_result)

        # print(result)

        return result

    i, j, direc_case = queue[depth]
    for case in direc_case:
        # print("=====")
        # for g in graph:
        #     print(g)
        # print("=====")

        temp_graph = copy.deepcopy(graph)
        
        for d in case:
            di, dj = d

            ni = i
            nj = j
            
            while True:
                ni += di
                nj += dj

                if ni < 0 or ni >= n or nj <0 or nj >= m:
                    break

                if temp_graph[ni][nj] == 6:
                    break

                temp_graph[ni][nj] = "#"

        draw_cctv_sight(n, m, temp_graph, queue, depth + 1)

    return result





n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

cctv_check(n, m, graph)
