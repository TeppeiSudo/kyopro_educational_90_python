from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

right = left = count = ans = 0
nums = defaultdict(int)
while right < N:
    if (count < K) or (nums[A[right]] > 0):
        nums[A[right]] += 1
        if nums[A[right]] == 1:
            count += 1
        right += 1
    else:
        nums[A[left]] -= 1
        if nums[A[left]] == 0:
            count -= 1
        left += 1
    ans = max(ans, right-left)

print(ans)