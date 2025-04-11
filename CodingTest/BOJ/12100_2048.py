from copy import deepcopy

def move(board, dir):
    def compress(line):
        new_line = [i for i in line if i != 0]
        for i in range(len(new_line)-1):
            if new_line[i] == new_line[i+1]:
                new_line[i] *= 2
                new_line[i+1] = 0
        new_line = [i for i in new_line if i != 0]
        return new_line + [0] * (n - len(new_line))
    
    new_board = [[0]*n for _ in range(n)]
    for i in range(n):
        if dir == 0:  # 위쪽
            line = [board[j][i] for j in range(n)]
            compressed = compress(line)
            for j in range(n):
                new_board[j][i] = compressed[j]
        elif dir == 1:  # 아래쪽
            line = [board[j][i] for j in range(n-1, -1, -1)]
            compressed = compress(line)
            for j in range(n):
                new_board[n-1-j][i] = compressed[j]
        elif dir == 2:  # 왼쪽
            line = board[i]
            compressed = compress(line)
            new_board[i] = compressed
        elif dir == 3:  # 오른쪽
            line = board[i][::-1]
            compressed = compress(line)
            new_board[i] = compressed[::-1]

    return new_board

def dfs(board, cnt):
    global answer
    if cnt == 5:
        answer = max(answer, max(map(max, board)))
        return
    for d in range(4):
        next_board = move(board, d)
        dfs(next_board, cnt+1)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dfs(board, 0)
print(answer)