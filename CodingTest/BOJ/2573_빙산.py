from collections import deque
N, M = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(N)]
time = 0
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

queue = deque()

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()
        cur = board[x][y]
        melt_cnt = 0
        
        for dx, dy in dir:  # 상하좌우
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0 and visited[nx][ny] == 0:
                    melt_cnt += 1
                if not visited[nx][ny] and board[nx][ny] != 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))

        if cur - melt_cnt <= 0:
            board[x][y] = 0
        else:
            board[x][y] = cur - melt_cnt
        

while True:
    ground_cnt = 0
    visited = [[0] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and visited[i][j] == 0:
                bfs(i, j)
                ground_cnt += 1
    
    if ground_cnt >= 2:
        print(time)
        break
    elif ground_cnt == 0:
        print(0)
        break
    time += 1