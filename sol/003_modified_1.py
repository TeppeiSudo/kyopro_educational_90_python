import collections


def getdist(graph, start):
    # 初期値を-1としておくとmax()の処理に弾かれるので、
    # 34行目と42行目で少し幸せになれる
    dist = [-1 for _ in range(N+1)] 

    Q = collections.deque()
    Q.append(start)
    dist[start] = 0

    while Q:
        pos = Q.pop()
        for to in graph[pos]:
            if dist[to] == -1:
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
dist1 = getdist(G, 1)
maxn1 = -1
for i, d in enumerate(dist1):
    if maxn1 < d:
        maxn1 = d
        maxid1 = i

#  Step #3. 頂点 maxid1 からの最短距離を求める
#  maxn2: 木の直径（最短距離の最大値）
dist2 = getdist(G, maxid1)
maxn2 = max(dist2)

#  Step #4. 出力
print(maxn2+1)