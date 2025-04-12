N = int(input())
lst = list(map(int, input().split()))

dp = [1] * N
prev = [-1] * N

for i in range(1, N):
    for j in range(i):
        if lst[j] < lst[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            prev[i] = j
max_len = max(dp)
last_idx = dp.index(max_len)
result = []

while last_idx != -1:
    result.append(lst[last_idx])
    last_idx = prev[last_idx]


result.reverse()
print(max_len)
print(*result)