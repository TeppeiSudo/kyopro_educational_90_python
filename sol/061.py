from collections import deque
Q = int(input())

que = deque()
for q in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        que.append(x)
    elif t == 2:
        que.appendleft(x)
    elif t == 3:
        print(que[-x])