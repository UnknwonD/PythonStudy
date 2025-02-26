from collections import deque

m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
q = deque()
ans = 0

visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j, 0))
            visited[i][j] = True

while q:
    y, x, ans = q.popleft()
    
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy
        
        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
            q.append((nx, ny, ans+1))
            visited[ny][nx] = True

trigger = False
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 0:
            trigger = True
            break

if trigger:
    print(-1)
    print(ans)
else:
    print(ans)

