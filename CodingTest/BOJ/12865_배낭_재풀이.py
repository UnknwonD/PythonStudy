import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0 for _ in range(K+1)] for _ in range(N)]

items = []
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))
items.sort(key=lambda x : (x[0], -x[1])) # 무게의 내림차순으로 정렬

# 초기값
for i in range(K+1):
    if i >= items[0][0]:
        dp[0][i] = items[0][1]

# 무게별 현재 넣을 수 있는 무게 중 가장 가치를 키울 수 있는 방법
for i in range(len(dp)):
    for w in range(len(dp[0])):
        if w >= items[i][0]:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-items[i][0]] + items[i][1])
        else:
            dp[i][w] = dp[i-1][w]

print(dp[-1][-1])