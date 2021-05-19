from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
cost = [[] for _ in range(N+1)]

for m in range(M):
    a, b, c = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    cost[a].append(c)
    cost[b].append(c)


def bfs(graph, cost, start):
    dist = [100000*M]*(N+1)
    dist[start] = 0
    que = deque([start])

    while que:
        pos = que.popleft()
        for nex, cos in zip(graph[pos], cost[pos]):
            if dist[nex] > dist[pos] + cos:
                dist[nex] = dist[pos] + cos
                que.append(nex)
    return dist


dist1 = bfs(graph, cost, 1)
distN = bfs(graph, cost, N)
for n in range(1, N+1):
    ans = dist1[n] + distN[n]
    print(ans)