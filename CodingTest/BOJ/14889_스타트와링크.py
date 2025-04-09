n = int(input())
perf = [list(map(int, input().split())) for _ in range(n)]
ans = int(1e10)

def cal(alst, blst):
    a, b = 0, 0
    for i in range(len(alst)):
        for j in range(i, len(blst)):
            a += perf[alst[i]][alst[j]]
            a += perf[alst[j]][alst[i]]
            
            b += perf[blst[i]][blst[j]]
            b += perf[blst[j]][blst[i]]
    return abs(a - b)

def dfs(cur, alst, blst):
    if cur == n:
        if len(alst) == len(blst):
            global ans
            ans = min(ans, cal(alst, blst))
        return
    
    if len(alst) < n // 2:
        dfs(cur+1, alst + [cur], blst)
    if len(blst) < n // 2:
        dfs(cur+1, alst, blst + [cur])

dfs(0, [], [])
print(ans)