from collections import deque

H, W = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
# 迷路の外周を壁(#)で囲う。
# rs,cs,rt,ctをデクリメントする必要がなくなり、
# さらに、28行目で少し幸せになれる。(maze[tx][ty] == "."がそのまま迷路外に出ない条件になる)
maze = ["#"*(W+2)]*(H+2)
for h in range(1, H+1):
    maze[h] = "#" + str(input()) + "#"

inf = float("inf")
dist = [inf] *4*(W+1)*(H+1)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
que = deque()
for i in range(4):
    dist[rs*W+cs+i*W*H] = 0
    que.append((rs, cs, i))
while que:
    u = que.pop()
    for i in range(4):
        tx = u[0] + dx[i]
        ty = u[1] + dy[i]
        cost = dist[u[0]*W+u[1]+u[2]*W*H] + 1 if u[2] != i else dist[u[0]*W+u[1]+u[2]*W*H]
        if (maze[tx][ty] == ".")and(dist[tx*W+ty+i*W*H] > cost):
            dist[tx*W+ty+i*W*H] = cost
            if u[2] != i:
                que.appendleft((tx, ty, i))
            else:
                que.append((tx, ty, i))

ans = inf
for i in range(4):
    ans = min(ans, dist[rt*W+ct+i*W*H])
print(ans) # this solution is acceptable (AC)