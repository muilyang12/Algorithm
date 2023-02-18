from collections import deque
import sys
input = sys.stdin.readline

# 1 : 빈 칸, 2 : 사과, 3 : 뱀
def get_time(n, k, graph, l, changes):
    snake = deque()

    x, y = 0, 0
    snake.append((x, y))
    graph[x][y] = 3
    time = 0

    now_d = 0
    direcs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    t_limit, d = changes.popleft()

    while True:
        if time == t_limit:
            if d == "L":
                now_d += -1
                
                if now_d == -4:
                    now_d = 0

            elif d == "D":
                now_d += 1

                if now_d == 4:
                    now_d = 0

            if changes:
                t_limit, d = changes.popleft()

        x, y = snake[-1]
        dx, dy = direcs[now_d][0], direcs[now_d][1]

        next_x = x + dx
        next_y = y + dy

        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
            time += 1
            break

        if graph[next_x][next_y] == 3:
            time += 1
            break

        elif graph[next_x][next_y] == 1:
            snake.append((next_x, next_y))
            graph[next_x][next_y] = 3

            temp_x, temp_y = snake.popleft()
            graph[temp_x][temp_y] = 1

            time += 1

        elif graph[next_x][next_y] == 2:
            snake.append((next_x, next_y))
            graph[next_x][next_y] = 3

            time += 1

    print(time)



n = int(input())
graph = [[1 for _ in range(n)] for _ in range(n)]

k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 2

l = int(input())

changes = deque()
for _ in range(l):
    t, d = input().split()
    t = int(t)
    
    changes.append((t, d))

get_time(n, k, graph, l, changes)

# 나 이거는 진짜 잘 푼 거 같다. queue 가 바로 떠오르네.