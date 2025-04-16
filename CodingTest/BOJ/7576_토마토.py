from collections import deque

N, M = map(int, input().split())
box = [[*map(int, input().split())] for _ in range(M)]
visited = [[False] * N for _ in range(M)]
ans = -1
q = deque()

for i in range(M):
    for j in range(N):
        if box[i][j] == 1:
            q.append((i, j, 0))
            visited[i][j] = True
            
while q:
    ci, cj, cost = q.popleft()
    ans = max(ans, cost)
    
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni, nj = ci + di, cj + dj
        
        if 0 <= ni < M and 0 <= nj < N:
            if not visited[ni][nj] and box[ni][nj] == 0:
                box[ni][nj] = 1
                visited[ni][nj] = True
                q.append((ni, nj, cost + 1))

flag = False
for i in range(M):
    for j in range(N):
        if box[i][j] == 0:
            flag = True
            break
        
ans = ans if not flag else -1
print(ans)