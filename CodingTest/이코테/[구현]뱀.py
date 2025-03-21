N = int(input())
mat = [[0 for _ in range(N)] for _ in range(N)]

K = int(input()) # 사과의 개수

for _ in range(K):
    row, col = map(int, input().split())
    mat[row-1][col-1] = 1
mat[0][0] = -1 # 시작위치

L = int(input())

senario = []
for _ in range(L):
    scen = input().split() # L : 왼쪽, D : 오른쪽
    senario.append((int(scen[0]), scen[1]))
senario.sort(key = lambda x: -x[0])

# dir = 0: 상, 1: 우, 2: 하, 3: 좌
dir_move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def move(pos, dir):
    tick_move = dir_move[dir]
    print(pos, tick_move)
    pos = [pos[0] + tick_move[0], pos[1] + tick_move[1]]
    return pos

# 방향 전환
def change_dir(dir, n_dir):
    if n_dir == 'L': #왼쪽
        dir = dir - 1 if dir - 1 >= 0 else 3
    elif n_dir == 'D': #오른쪽
        dir = dir + 1 if dir + 1 <= 3 else 0
    return dir

from collections import deque

now_dir = 1
time = 0
pos = [0, 0]
body = deque()
body.append((0, 0))

while True:
    pos = move(pos, now_dir)
    time += 1
    print(f"시간 : {time}, 현재 위치 : {pos}, 방향 : {now_dir}, 몸길이 : {len(body)}")

    # 게임 오버 확인
    if (0 > pos[0]) or (len(mat)-1 < pos[0]) or (0 > pos[1]) or (len(mat[0])-1 < pos[1]): # 맵 이탈
        print(time)
        break
    elif mat[pos[0]][pos[1]] == -1: # 몸에 부딪힘
        print(time)
        break

    if mat[pos[0]][pos[1]] == 1: # 사과가 있는 것
        body.append(pos) # 몸 추가
        mat[pos[0]][pos[1]] = -1

    else: # 사과가 없음
        y, x = body.popleft() # 꼬리 제거
        mat[y][x] = 0

        body.append(pos)
        mat[pos[0]][pos[1]] = -1
        
    if (len(senario) != 0) and (senario[-1][0] == time):
        nt, new_dir = senario.pop()
        now_dir = change_dir(now_dir, new_dir)

        print(f"방향 전환 : 시점 {nt}, 다음 방향 {new_dir}, 바뀐 방향 {now_dir}")