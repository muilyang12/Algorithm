from collections import deque
import sys
input = sys.stdin.readline

def get_count(n, l, r, graph):
    count = 0
    
    while True:
        groups = []
        visited = [[False for _ in range(n)] for _ in range(n)]

        queue = deque()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        there_is_change = False

        for i in range(n):
            for j in range(n):
                if visited[i][j]:
                    continue

                g_num = len(groups)

                groups.append([(i, j)])
                queue.append((i, j, g_num))
                visited[i][j] = True

                while queue:
                    x, y, g_num = queue.popleft()

                    for k in range(4):
                        next_x = x + dx[k]
                        next_y = y + dy[k]

                        if next_x < 0 or next_x > n - 1 or next_y < 0 or next_y > n - 1:
                            continue

                        if visited[next_x][next_y]:
                            continue

                        diff = abs(graph[next_x][next_y] - graph[x][y])
                        if diff >= l and diff <= r:
                            groups[g_num].append((next_x, next_y))
                            queue.append((next_x, next_y, g_num))
                            visited[next_x][next_y] = True

                            there_is_change = True

        for group in groups:
            if len(group) > 1:
                sum = 0
                for g in group:
                    x, y = g
                    sum += graph[x][y]

                sum = sum // len(group)

                for g in group:
                    x, y = g
                    graph[x][y] = sum

        if there_is_change:
            count += 1

        else:
            print(count)
            return



n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

get_count(n, l, r, graph)

# 이 코드의 경우 Python3 로 제출하면 시간초과가 출력되는 반면, PyPy3 로 제출하면 통과된다.
# 잘 봤을 때 여러 개의 for 문이 겹쳐져 있는 것이 문제의 주 원인이라고 판단이 들 경우,
# PyPy3 로 꼭 돌려보자.

# https://www.acmicpc.net/problem/1931
# https://www.acmicpc.net/problem/14502
# https://www.acmicpc.net/problem/3190
# https://www.acmicpc.net/problem/15686