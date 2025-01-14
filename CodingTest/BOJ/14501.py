def dfs(now, earn):
    global ans
    # 종료조건 now가 N보다 크거나 작아지는 경우
    if now >= N:
        ans = max(ans, earn)
        return 

    if now + T[now] <= N:
        dfs(now + T[now], P[now] + earn)
    dfs(now+1, earn)

N = int(input())
T, P = [0] * N, [0] * N

for i in range(N):
    T[i], P[i] = map(int, input().split())

ans = 0
dfs(0, 0)
print(ans)
