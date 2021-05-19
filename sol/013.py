from heapq import heappop, heappush, heapify

def dijkstra(start):
    dist = [1<<60]*(N+1)
    dist[start] = 0
    Q = [(0, start)]
    heapify(Q)

    while Q:
        pos = heappop(Q)[1]
        for i in range(len(G[pos])):
            to, cost = G[pos][i]
            if dist[to] > dist[pos] + cost:
                dist[to] = dist[pos] + cost
                heappush(Q, (dist[to], to))
    return dist

# Step #1. 入力
N, M = map(int, input().split())
# 入力
A, B, C = [0]*(M+1), [0]*(M+1), [0]*(M+1)
# グラフ・最短距離
dist1, distN = [0]*(N+1), [0]*(N+1)
G = [[] for _ in range(N+1)]

for i in range(1, M+1):
    A[i], B[i], C[i] = map(int, input().split())
    G[A[i]].append((B[i], C[i]))
    G[B[i]].append((A[i], C[i]))

# Step #2. 頂点 1 からの最短距離を求める
dist = dijkstra(1)
for i in range(1, N+1):
    dist1[i] = dist[i]

# Step #3. 頂点 N からの最短距離を求める
dist = dijkstra(N)
for i in range(1, N+1):
    distN[i] = dist[i]

# Step #4. 出力
for i in range(1, N+1):
    ans = dist1[i] + distN[i]
    print(ans)