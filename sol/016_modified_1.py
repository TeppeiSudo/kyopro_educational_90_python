N = int(input())
A, B, C = map(int, input().split())

ans = N
for na in range(10000):
        for nb in range(10000):
            if (N - A*na - B*nb >=0) and ((N - A*na - B*nb)%C == 0):
                nc = (N - A*na - B*nb)//C
                ans = min(ans, na+nb+nc)

print(ans)