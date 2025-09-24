import sys

# 입력 처리
n = int(sys.stdin.readline())
find_num = int(sys.stdin.readline())

# N x N 보드 생성
board = [[0] * n for _ in range(n)]

# 방향 설정: 아래 -> 오른쪽 -> 위 -> 왼쪽 순서
# (y축 변화량, x축 변화량)
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 시작 위치 및 초기값 설정
x, y = 0, 0
cur_dir = 0
num = n * n

# 찾으려는 숫자의 좌표를 저장할 변수
ans_pos = (0, 0)

# N*N부터 1까지 숫자를 채워나감
while num > 0:
    # 현재 위치에 숫자 채우기
    board[y][x] = num
    
    # 만약 현재 숫자가 찾으려는 숫자라면 좌표 저장 (1-based index)
    if num == find_num:
        ans_pos = (y + 1, x + 1)

    # 다음 위치 계산
    ny, nx = y + dirs[cur_dir][0], x + dirs[cur_dir][1]

    # 다음 위치가 격자를 벗어나거나, 이미 숫자가 채워져 있다면 방향 전환
    if not (0 <= ny < n and 0 <= nx < n) or board[ny][nx] != 0:
        cur_dir = (cur_dir + 1) % 4
    
    # 실제 위치 업데이트
    y += dirs[cur_dir][0]
    x += dirs[cur_dir][1]
    
    num -= 1

# 결과 출력
for row in board:
    print(*row)
print(*ans_pos)