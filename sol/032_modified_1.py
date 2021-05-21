from itertools import permutations

N = int(input())
A = [[0]*N for _ in range(N)]
for n in range(N):
    A[n] = list(map(int, input().split()))

M = int(input())
kenaku = [[False]*N for _ in range(N)]
for m in range(M):
    x, y = map(int, input().split())
    # Aの添字の範囲に合わせてx,yを−１する
    kenaku[x-1][y-1] = True
    kenaku[y-1][x-1] = True

runner = list(range(N))
ans = 1<<30
for run_order in permutations(runner, N):
    flag = True
    for n in range(N-1):
        if kenaku[run_order[n]][run_order[n+1]]:
            flag = False
    if flag:
        time = sum([A[run_order[n]][n] for n in range(N)])
        ans = min(ans, time)

if ans == 1<<30:
    print(-1)
else:
    print(ans)