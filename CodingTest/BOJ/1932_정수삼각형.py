N = int(input())
arr = []

for _ in range(N):
    arr.append([*map(int, input().split())])
    
if N == 1:
    print(arr[0][0])
else:
    dp = [[0] * N for _ in range(N)]

    dp[-1] = arr[-1]

    for i in range(N-2, 0, -1):
        for j in range(len(arr[i])):
            dp[i][j] = max(arr[i][j] + dp[i+1][j+1], arr[i][j] + dp[i+1][j])

    print(max(dp[1]) + arr[0][0])