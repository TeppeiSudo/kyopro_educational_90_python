import sys
sys.setrecursionlimit(500*500)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
rgraph = [[] for _ in range(N+1)]

for m in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    rgraph[b].append(a)

used = [False]*(N+1)
union = []
def dfs1(pos):
    used[pos] = True
    for nex in graph[pos]:
        if not used[nex]:
            dfs1(nex)
    union.append(pos)

def dfs2(pos, cnts):
    used[pos] = True
    cnts += 1
    for nex in rgraph[pos]:
        if used[nex] == False:
            cnts = dfs2(nex, cnts)
    return cnts

for i in range(1, N+1):
    if used[i] == False:
        dfs1(i)

ans = 0
union = list(reversed(union))
used = [False]*(N+1)
for i in union:
    if used[i]:
        continue
    else:
        cnts = dfs2(i, 0)
        ans += cnts * (cnts - 1) // 2
print(ans)