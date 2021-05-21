from itertools import permutations

# Step #1. Input
N = int(input())
A = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    a = [0]
    a.extend(list(map(int, input().split())))
    # 上の二行を挟まないと,A[i][j]のjの範囲が0--N-1になってしまうので注意
    A[i] = a

M = int(input())
X, Y = [0]*(M+1), [0]*(M+1)
for i in range(1, M+1):
    X[i], Y[i] = map(int, input().split())

# Step #2. Init
kenaku = [[False]*(N+1) for _ in range(N+1)]
for i in range(1, M+1):
    kenaku[X[i]][Y[i]] = True
    kenaku[Y[i]][X[i]] = True

# Step #3. Brute Force
ans = 1<<30
vect = list(range(1, N+1))
for vec in permutations(vect, N):
    flag = True
    sum = 0
    for i in range(N-1):
        if kenaku[vec[i]][vec[i+1]]:
            flag = False
    for i in range(N):
        sum += A[vec[i]][i+1]
    if flag:
        ans = min(ans, sum)

# Step #4. Output The Answer
if ans == 1<<30:
    ans = -1
print(ans)