# 가장 긴 증가하는 부분수열
# https://www.acmicpc.net/problem/11053

n = int(input())
seq = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))