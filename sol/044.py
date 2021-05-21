N, Q = map(int, input().split())
A = list(map(int, input().split()))

shifts = 0
for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        x -= 1
        y -= 1
        A[(x+shifts)%N], A[(y+shifts)%N] = A[(y+shifts)%N], A[(x+shifts)%N]
    elif t == 2:
        shifts = (shifts + N - 1) % N
    elif t ==3:
        x -= 1
        print(A[(x+shifts)%N])