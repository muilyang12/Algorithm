import sys
input = sys.stdin.readline

shapes = [
    [[(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (0, 1), (0, 2), (0, 3)]],
    [[(0, 0), (0, 1), (1, 0), (1, 1)]],
    [[(0, 0), (1, 0), (2, 0), (2, 1)], [(0, 0), (1, 0), (2, 0), (2, -1)], [(0, 0), (0, 1), (0, 2), (1, 2)], [(0, 0), (-1, 0), (-1, 1), (-1, 2)], [(0, 0), (0, 1), (0, 2), (-1, 2)], [(0, 0), (1, 0), (1, 1), (1, 2)], [(0, 0), (0, 1), (1, 1), (2, 1)], [(0, 0), (0, -1), (1, -1), (2, -1)]],
    [[(0, 0), (1, 0), (1, 1), (2, 1)], [(0, 0), (1, 0), (1, -1), (2, -1)], [(0, 0), (0, 1), (1, 1), (1, 2)], [(0, 0), (0, 1), (-1, 1), (-1, 2)]],
    [[(0, 0), (0, 1), (0, 2), (1, 1)], [(0, 0), (1, 0), (2, 0), (1, 1)], [(0, 0), (0, 1), (0, 2), (-1, 1)], [(0, 0), (0, 1), (-1, 1), (1, 1)]]
]
def find_max(n, m, graph):
    result = -99999

    for x in range(n):
        for y in range(m):
            
            for shape in shapes:
                for directions in shape:
                    temp_sum = 0
                    lll = []

                    for direction in directions:
                        dx, dy = direction

                        nx = x + dx
                        ny = y + dy

                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            break

                        temp_sum += graph[nx][ny]
                        lll.append(graph[nx][ny])

                    result = max(result, temp_sum)

    print(result)





n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
find_max(n, m, graph)
