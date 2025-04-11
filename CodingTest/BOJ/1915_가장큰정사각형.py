N, M = map(int, input().split())
data = [list(map(int, list(input()))) for _ in range(N)]

dp = [[0]*M for _ in range(N)] 
ans = 0

for y in range(N):
    for x in range(M):
        if data[y][x] == 1:
            if x == 0 or y == 0:
                dp[y][x] = 1
            else:
                dp[y][x] = min(dp[y-1][x], dp[y][x-1], dp[y-1][x-1]) + 1
        
        ans = max(dp[y][x], ans)

print(ans*ans)
