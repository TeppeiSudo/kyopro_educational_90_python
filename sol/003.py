import collections


def getdist(start):
    # 幅優先探索（BFS）により、最短距離を計算
    inf = 1<<29
    dist = [inf for i in range(N+1)]

    Q = collections.deque()
    Q.append(start)
    dist[start] = 0

    while Q:
        pos = Q.pop()
        for to in G[pos]:
            if dist[to] == inf:
                dist[to] = dist[pos] + 1
                Q.append(to)
    return dist


#  Step #1. 入力
N = int(input())
G = [[] for _ in range(N+1)]
for i in range(N-1):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

#  Step #2. 頂点 1 からの最短距離を求める
#  maxid1: 頂点 1 から最も離れている（最短距離が長い）頂点
dist1 = getdist(1)
maxn1, maxid1 = -1, -1
for i in range(1, N+1):
    if maxn1 < dist1[i]:
        maxn1 = dist1[i]
        maxid1 = i

#  Step #3. 頂点 maxid1 からの最短距離を求める
#  maxn2: 木の直径（最短距離の最大値）
dist2 = getdist(maxid1)
maxn2 = -1
for i in range(1, N+1):
    maxn2 = max(maxn2, dist2[i])

#  Step #4. 出力
print(maxn2+1)