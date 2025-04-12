from copy import deepcopy

# 입력
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# CCTV 방향 정의 (상, 우, 하, 좌 = 0,1,2,3)
cctv_dirs = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

# 방향 벡터 (상 우 하 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# CCTV 위치 수집
cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            cctvs.append((i, j, board[i][j]))

min_blind = int(1e9)

# 감시 구역 채우기
def fill(temp, x, y, directions):
    for d in directions:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if not (0 <= nx < N and 0 <= ny < M): break
            if temp[nx][ny] == 6: break
            if temp[nx][ny] == 0:
                temp[nx][ny] = -1  # 감시 표시

# DFS로 모든 경우 탐색
def dfs(depth, arr):
    global min_blind
    if depth == len(cctvs):
        count = sum(row.count(0) for row in arr)
        min_blind = min(min_blind, count)
        return

    x, y, type_ = cctvs[depth]
    for dirs in cctv_dirs[type_]:
        temp = deepcopy(arr)
        fill(temp, x, y, dirs)
        dfs(depth + 1, temp)

# 실행
dfs(0, board)
print(min_blind)