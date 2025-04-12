import sys
input = sys.stdin.readline
ans = []
while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    
    data = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * M for _ in range(N)]
    res = 0
    for y in range(N):
        for x in range(M):
            if data[y][x] == 1:
                dp[y][x] = min(dp[y][x-1], dp[y-1][x], dp[y-1][x-1]) + 1
                res = max(dp[y][x], res)
    ans.append(res) 

for a in ans:
    print(a)