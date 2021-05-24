from collections import defaultdict

# Step #1. Input
N, K = map(int, input().split())
input_line = list(map(int, input().split()))
A = [0]
A.extend(input_line)

# Step #2. Shakutori
cr = 1; cnt = 0; ans = 0
nums = defaultdict(int)
for i in range(1, N+1):
    while cr <= N:
        if (nums[A[cr]] == 0)and(cnt == K):
            break
        if nums[A[cr]] == 0:
            cnt += 1
        nums[A[cr]] += 1
        cr += 1

    ans = max(ans, cr - i)
    if nums[A[i]] == 1:
        cnt -= 1
    nums[A[i]] -= 1

# Step #3. Output The Answer
print(ans)