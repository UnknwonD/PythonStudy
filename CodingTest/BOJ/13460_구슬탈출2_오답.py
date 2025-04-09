# 시뮬레이션 진행
def dfs(cnt, b_pos, r_pos):
    print(f"시행횟수 {cnt}, 파란공 {b_pos}, 빨간공 {r_pos}, 목표 {goal}")
    # 종료조건
    if (cnt > 10) or (b_pos == goal) or (r_pos == goal):
        global ans
        if cnt > 10:
            ans = max(ans, -1)
        elif r_pos == goal and b_pos != goal:
            ans = min(ans, cnt)
        return

    # 하부호출
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        print(f"이동 방향 {dx}, {dy}")
        nbx, nby = b_pos[0] + dx, b_pos[1] + dy
        nrx, nry = r_pos[0] + dx, r_pos[1] + dy
        
        # 둘 중 하나라도 이동할 수 있으면 이동 수행
        if ((map[nby][nbx] != '#') or (map[nry][nrx] != '#')) and (cnt < 3):
            n_b_pos, n_r_pos = move(dx, dy, b_pos, r_pos)
            dfs(cnt+1, n_b_pos, n_r_pos)

# dx, dy방향으로 구슬을 이동시키는 함수
def move(dx, dy, b_pos, r_pos):
    
    def check(pos1, pos2, b_fin, r_fin):
        nbx, nby = pos1[0] + dx, pos1[1] + dy
        nrx, nry = pos2[0] + dx, pos2[1] + dy
        
        # 이동 멈춘 구슬이 다음 위치에 있는지 확인
        if (b_fin and (b_pos == [nrx, nry])) or (r_fin and (r_pos == [nbx, nby])):
            return True, True
        
        return (map[nby][nbx] == '#'), (map[nry][nrx] == '#')
    
    # 이동 수행
    b_fin, r_fin = check(b_pos, r_pos, False, False)
    bx, by = b_pos[0], b_pos[1]
    rx, ry = r_pos[0], r_pos[1]
    
    # 먼저 이동할 구술 선택
    if dx == 1: # 오른쪽
        b_first = bx > rx
    elif dx == -1: # 왼쪽
        b_first = bx < rx
    elif dy == 1: # 아래
        b_first = by > ry
    else: # 위
        b_first = by < ry
        
    # 구슬 이동 (구슬이 이동할 수 없을 때까지)
    while not (b_fin and r_fin):
        # 다음 이동 수행이 가능한지 확인
        b_next, r_next = check((bx, by), (rx, ry), b_fin, r_fin)
        
        b_fin = (b_next | b_fin)
        r_fin = (r_next | r_fin)
        
        if b_fin and r_fin:
            break
        if b_fin: # 빨간색만
            rx, ry = rx + dx, ry + dy
        elif r_fin: # 파란색만
            bx, by = bx + dx, by + dy
        else: # 둘 다 이동
            rx, ry = rx + dx, ry + dy
            bx, by = bx + dx, by + dy
            
        if [rx, ry] == goal:
            r_fin = True
        if [bx, by] == goal:
            b_fin = True
        
        if map[by][bx] == 'O':
            b_fin = True
        if map[ry][rx] == 'O':
            r_fin = True
        
        
    return [bx, by], [rx, ry]

# 탈출구와 구슬들의 위치를 찾아내는 함수
def find_r_b():
    goal, b_pos, r_pos = 0, 0, 0
    for i in range(n):
        for j in range(m):
            if map[i][j] in ('#', '.'):
                continue
            elif map[i][j] == 'O':
                goal = [i, j]
            elif map[i][j] == 'B':
                b_pos = [i, j]
                map[i][j] = '.'
            elif map[i][j] == 'R':
                r_pos = [i, j]
                map[i][j] = '.'
    return goal, b_pos, r_pos
    
n, m = map(int, input().split())
map = [list(input()) for _ in range(n)]
ans = int(1e10)

goal, b_pos, r_pos = find_r_b()
dfs(0, b_pos, r_pos)

print(ans)