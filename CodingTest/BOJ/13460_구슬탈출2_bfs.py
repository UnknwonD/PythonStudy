from collections import deque

def move(x, y, dx, dy, board):
    count = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs(board, rx, ry, bx, by):
    visited = set()
    queue = deque([(rx, ry, bx, by, 0)])
    visited.add((rx, ry, bx, by))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth >= 10:
            break
        for dx, dy in directions:
            nrx, nry, r_count = move(rx, ry, dx, dy, board)
            nbx, nby, b_count = move(bx, by, dx, dy, board)

            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                return depth + 1

            if nrx == nbx and nry == nby:
                if r_count > b_count:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                queue.append((nrx, nry, nbx, nby, depth + 1))
    return -1

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

rx = ry = bx = by = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
            board[i][j] = '.'
        elif board[i][j] == 'B':
            bx, by = i, j
            board[i][j] = '.'

result = bfs(board, rx, ry, bx, by)
print(result)