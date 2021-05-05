def solve(M):
    cnt = pre = 0
    for i in range(N):
        if (A[i] - pre >= M)and(L - A[i] >= M):
            cnt +=  1
            pre = A[i]
    if cnt >= K:
        return True
    return False


#  Step #1. 入力
N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

#  Step #2. 答えで二分探索（めぐる式二分探索）
#  https://qiita.com/drken/items/97e37dd6143e33a64c8c
left = -1
right = L + 1
while (right - left > 1):
    mid = int(left + (right - left) / 2)
    if not solve(mid):
        right = mid
    else:
        left = mid
print(left)