from collections import deque, defaultdict

H, W = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
rs -= 1; cs -= 1; rt -= 1; ct -= 1
maze = [""]*H
for h in range(H):
    maze[h] = str(input())

inf = float("inf")
dist = [[[inf, inf, inf, inf] for _ in range(W)] for _ in range(H)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
que = deque()
for i in range(4):
    dist[rs][cs][i] = 0
    que.append((rs, cs, i))
while que:
    u = que.pop()
    for i in range(4):
        tx = u[0] + dx[i]
        ty = u[1] + dy[i]
        cost = dist[u[0]][u[1]][u[2]] + 1 if u[2] != i else dist[u[0]][u[1]][u[2]]
        if (0 <= tx < H)and(0 <= ty < W)and(maze[tx][ty] == ".")and(dist[tx][ty][i] > cost):
            dist[tx][ty][i] = cost
            if u[2] != i:
                que.appendleft((tx, ty, i))
            else:
                que.append((tx, ty, i))

ans = min(dist[rt][ct])
print(ans)