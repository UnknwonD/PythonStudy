N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# ← 방향 기준 비율 (dx, dy, ratio)
sand_spead = [
    (-1, -1, 0.1), (0, -1, 0.07), (1, -1, 0.01),
    (-1, 1, 0.1), (0, 1, 0.07), (1, 1, 0.01),
    (0, -2, 0.02), (0, 2, 0.02),
    (-2, 0, 0.05), (-1, 0, 0)  # 마지막 -1, 0은 'a' 위치
]

def rotate_sand(dx, dy, dir):
    if dir == 0: return dx, dy
    elif dir == 1: return dy, -dx
    elif dir == 2: return -dx, -dy
    elif dir == 3: return -dy, dx

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 좌 하 우 상

ci, cj = N // 2, N // 2
cnt, cnt_mx = 0, 1
flag = False
dir = 0
ans = 0

while (ci, cj) != (0, 0):
    ci += dirs[dir][0]
    cj += dirs[dir][1]
    cnt += 1
    
    if board[ci][cj] != 0:
        sand_total = board[ci][cj]
        board[ci][cj] = 0
        sand_sum = 0

        for dx, dy, ratio in sand_spead:
            rdx, rdy = rotate_sand(dx, dy, dir)
            ny, nx = ci + rdy, cj + rdx  # row(col) 기준으로!

            if ratio != 0:
                spread = int(sand_total * ratio)
                sand_sum += spread
            else:
                spread = sand_total - sand_sum  # 마지막 남은 모래

            if 0 <= ny < N and 0 <= nx < N:
                board[ny][nx] += spread
            else:
                ans += spread

    if cnt == cnt_mx:
        cnt = 0
        dir = (dir + 1) % 4
        if flag:
            cnt_mx += 1
            flag = False
        else:
            flag = True

print(ans)
