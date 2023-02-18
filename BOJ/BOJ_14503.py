import sys
input = sys.stdin.readline

# 북, 동, 남, 서
d_arr = [0, 1, 2, 3]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

visited = []
count = 0

def get_count(n, m, r, c, d, graph):
    global visited
    global count

    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 0

    dfs(n, m, r, c, d, graph)

    print(count)

def dfs(n, m, r, c, d, graph):
    global visited
    global count

    visited[r][c] = True
    graph[r][c] = count + 2
    count += 1

    print(r, c)
    for g in graph:
        print(g)
    print(count)
    print()

    for i in range(1, 5):
        next_r = r + dr[d - i]
        next_c = c + dc[d - i]

        if next_r < 0 or next_r >= n or next_c < 0 or next_c >= m:
            continue

        if graph[next_r][next_c] == 1:
            continue

        if visited[next_r][next_c]:
            continue

        dfs(n, m, next_r, next_c, d_arr[d - i], graph)



n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for _ in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)

get_count(n, m, r, c, d, graph)

# 근데 솔직히 문제 설명이 좀 어색한 거 아닌가.....

# 2 - c 의 경우는 2 - b 에서의 방향 전환을 네 번 반복해야 사방에 청소할 곳이 없다는 것을 알 수 있는 거 아닌가.
# 만약 네 번의 방향 전환을 해야 알 수 있는 것이라면, 네 번의 방향 전환 끝에 바라보는 방향은 해당 칸에 들어왔을 때의 방향과 달라지게 될테고.
# 그래서 나는 해당 칸에 들어온 방향을 기억해서 자동으로 뒤로 나가는 것이라고 생각했었는데 ㅠㅠㅠㅠㅠ 그런데 문제의 답에 따르면 '사방에
# 청소할 곳이 없다는 것은 굳이 네 번의 방향 전환을 안해도 딱 봐도 아니까 들어온 방향 그대로 나가자.' 이것을 의도 한 것 같네.