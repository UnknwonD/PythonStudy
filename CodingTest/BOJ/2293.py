n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)], reverse=True)

dp = [0] * (k+1)
dp[0] = 1

for coin in coins:
    for j in range(coin, k+1):
        dp[j] += dp[j-coin]

print(dp[k])