from collections import deque

N, M = map(int, input().split())
data = [[*map(int, list(input()))] for _ in range(N)]

visited = [[False] * M for _ in range(N)]

q = deque()
q.append((0, 0, 1))
visited[0][0] = True


while q:
    ci, cj, cost = q.popleft()
    
    if ci == N-1 and cj == M-1:
        print(cost)
        break

    directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
    
    for di, dj in directions:
        ni, nj = ci + di, cj + dj
        
        if 0 <= ni < N and 0 <= nj < M:
            if not visited[ni][nj] and data[ni][nj] == 1:
                q.append((ni, nj, cost+1))
                visited[ni][nj] = True