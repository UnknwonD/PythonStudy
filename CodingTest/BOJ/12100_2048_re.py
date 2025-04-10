from collections import deque

# 이동 처리 - 같은 숫자 만나면 결합시켜주기
# 한 번 이동에는 한 번의 결합만 가능함
def move(map, dir):
    max_val = 0
    
    for i in range(n):
        for j in range(n):
            if map[j][i] == 0:
                continue
            if map[j][i] == -1:
                map[j][i] = 0
            
            nx, ny = i, j
            
            # 1. 0이 아닐 때까지 이동
            while map[ny][nx] == 0:
                # 범위 밖으로 나가는 경우 종료
                if 0 > nx or n <= nx or 0 > ny or n <= ny:
                    nx, ny = i - dir[0], j - dir[1]
                    break
                nx, ny = i + dir[0], j + dir[1]
            
            # 이동을 못했다면 0이 없거나, 끝에 위치한 경우
            if nx == i and ny == j:
                if map[ny][nx] != 0: # 애초에 0이 없어서 이동을 못한 경우,
                    nx, ny = i + dir[0], j + dir[1]
                else: # 끝에 위치한 경우
                    continue
            
            # 범위 밖으로 나간경우, 무시
            if 0 > nx or n <= nx or 0 > ny or n <= ny:
                continue
            
            if map[ny][nx] == 0:
                map[ny][nx] = map[j][i]
                map[j][i] = 0
            
            # 같은 숫자 만나면, 합쳐줌
            elif map[ny][nx] == map[j][i]:
                map[ny][nx] += 1
                map[ny-dir[1]][nx-dir[0]] = -1 # 합쳐졌다는 표시 해줌
                map[j][i] = 0
            # -1을 만나는 경우, 그 곳으로 이동시켜줌
            elif map[ny][nx] == -1:
                map[ny][nx] = map[j][i]
                map[j][i] = 0
            
            max_val = max(max_val, map[ny][nx])
    return map, max_val

# 탐색
def bfs():
    global map_2024
    queue = deque()
    ans = 0
    tmpcnt = 0
    directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
    queue.append((map_2024, 0))
    
    while queue:
        n_map, cnt = queue.popleft()
        
        if cnt > 5:
            continue
        
        for dx, dy in directions:
            next_map, max_val = move(n_map, (dx, dy))
            queue.append((next_map, cnt+1))
            ans = max(max_val, ans)
            if tmpcnt < 200:
                print(next_map, f"방향 : {dx}, {dy}, 시행 횟수 : {cnt}")
            tmpcnt += 1
    
    return ans
        
        
from math import log2
n = int(input())
map_2024 = [list(map(int, input().split())) for _ in range(n)]


# 문제 : 1인 경우 필요가 없음 (입력은 1이 없음)
for i in range(n):
    for j in range(n):
        if map_2024[i][j] != 0:
            map_2024[i][j] = int(log2(map_2024[i][j]))

print(2**bfs())


