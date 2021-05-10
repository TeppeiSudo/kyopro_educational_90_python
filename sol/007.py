# Python にはlower_boundが標準では用意されていないので
# 二分探索で実装
def lower_bound(A, target):
    left = 0
    right = len(A)-1
    while left+1 <  right:
        mid = (left + right)//2
        if A[mid] > target:
            right = mid
        else:
            left = mid
    return right


inf = 20000000000

# Step #1. Input
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = [0]*Q
for i in range(Q):
    B[i] = int(input())

# Step #2. Sorting
A.sort()

# Step #3. Binary Search
for i in range(Q):
    pos1 = lower_bound(A, B[i])
    diff1 = diff2 = inf
    if pos1 <= N-1:
        diff1 = abs(B[i] - A[pos1])
    if pos1 >= 1:
        diff2 = abs(B[i] - A[pos1 - 1])
    print(min(diff1, diff2))