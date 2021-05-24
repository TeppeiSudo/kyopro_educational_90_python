# Step #1. Input
N = int(input())
paper = [[0]*(1001) for _ in range(1001)]

# Step #2. Imos Method in 2D
for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    paper[lx][ly] += 1
    paper[rx][ly] -= 1
    paper[lx][ry] -= 1
    paper[rx][ry] += 1

for i in range(1001):
    for j in range(1, 1001):
        paper[i][j] += paper[i][j-1]

for i in range(1, 1001):
    for j in range(1001):
        paper[i][j] += paper[i-1][j]

# Step #3. Count Number
ans = [0]*(N+1)
for i in range(1001):
    for j in range(1001):
        ans[paper[i][j]] += 1

# Step #4. Output The Answer
print(*ans[1:], sep="\n")