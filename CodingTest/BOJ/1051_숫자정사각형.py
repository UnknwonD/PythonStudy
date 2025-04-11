N, M = map(int, input().split())
data = [list(map(int, list(input()))) for _ in range(N)]

search_range = min(N, M)
ans = 1

for i in range(search_range, 0, -1):
    for y in range(N):
        if (y+i-1) >= N:
            break
        
        for x in range(M):
            if (x+i-1) >= M:
                break
            
            if data[y][x] == data[y][x+i-1] == data[y+i-1][x] == data[y+i-1][x+i-1]:
                ans = max(ans, i)
                break
        if i == ans:
            break
    if i == ans:
        break

print(ans*ans)