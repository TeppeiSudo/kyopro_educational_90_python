# 入力
N = int(input())

C = [0]*(N+1)
P = [0]*(N+1)

#累積和
Sum1 = [0]*(N+1)
Sum2 = [0]*(N+1)

# Step #1. 入力
for i in range(1, N+1):
    C[i], P[i] = map(int, input().split())
    
Q = int(input())
L = [0]*(Q+1)
R = [0]*(Q+1)
for i in range(1, Q+1):
    L[i], R[i] = map(int, input().split())

# Step #2. 1 組・2 組それぞれの累積和を取る
for i in range(1, N+1):
    Sum1[i] = Sum1[i-1]
    Sum2[i] = Sum2[i-1]
    if C[i] == 1:
        Sum1[i] += P[i]
    elif C[i] == 2:
        Sum2[i] += P[i]

# Step #3. クエリに答える
for i in range(1, Q+1):
    Answer1 = Sum1[R[i]] - Sum1[L[i] - 1]
    Answer2 = Sum2[R[i]] - Sum2[L[i] - 1]
    print(Answer1, Answer2)