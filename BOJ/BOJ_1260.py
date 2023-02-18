from collections import deque
import sys
input = sys.stdin.readline

def dfs(node, line, start, cons):
    visited[start] = True
    print(start, end=" ")

    for con in cons[start]:
        if not visited[con]:
            dfs(node, line, con, cons)

def bfs(node, line, start, cons):
    visited = [False] * (node + 1)

    queue = deque()
    queue.append(start)
    visited[start] = True
    print(start, end=" ")

    history = []

    while queue:
        now = queue.popleft()

        for con in cons[now]:
            if not visited[con]:
                queue.append(con)
                visited[con] = True
                print(con, end=" ")        



node, line, start = map(int, input().split())
cons = [[] for _ in range(node + 1)]
for _ in range(line):
    fr, to = map(int, input().split())
    cons[fr].append(to)
    cons[to].append(fr)

for con in cons:
    con.sort()

# visited = [False] * (node + 1)
visited = [False for _ in range(node + 1)]
dfs(node, line, start, cons)
print()
bfs(node, line, start, cons)

# 탐색 -> 순차탐색, 이분탐색, BFS, DFS