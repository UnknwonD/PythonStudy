import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mem = list(map(int, input().split()))
cost = list(map(int, input().split()))

total_cost = sum(cost)
# dp[i]: 비용이 i일 때 확보할 수 있는 최대 메모리
dp = [0] * (total_cost + 1)

for i in range(N):
    m = mem[i]
    c = cost[i]
    for j in range(total_cost, c - 1, -1):
        dp[j] = max(dp[j], dp[j - c] + m)

# 최소 비용 찾기
for i in range(total_cost + 1):
    if dp[i] >= M:
        print(i)
        break