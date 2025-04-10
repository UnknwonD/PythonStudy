from collections import deque

# 이동 처리 - 같은 숫자 만나면 결합시켜주기
# 한 번 이동에는 한 번의 결합만 가능함
def move(map, dir):
    max_val = 0
    
    for i in range(n):
        for j in range(n):
            if map[j][i] == 0:
                continue
            cur = map[j][i]
            
            
            # 해당 블록이 움직일 수 없을 때까지 이동
            # 2, 0에서 못 나감
            while True:
                nx, ny = i + dir[0], j + dir[1]
                
                # 범위 밖으로 나가는 경우
                if 0 > nx or n <= nx or 0 > ny or n <= ny:
                    break
                print(nx, ny, map[ny][nx], cur)
                
                # 이미 합쳐진 블록인 경우 -> 그냥 그 위치로 옮겨줌
                if map[ny][nx] == -1:
                    map[ny][nx] = map[ny-dir[1]][nx-dir[0]]
                    
                    map[ny-dir[1]][nx-dir[0]] = 0
                    break
                
                if map[ny][nx] != 0:
                    # 합칠 수 있는 경우에 합쳐줌
                    # 더해서 다음 블록에 넣어주고, 직전 블록에 -1을 넣어줌
                    if map[ny][nx] == map[ny-dir[1]][nx-dir[0]]:
                        map[ny-dir[1]][nx-dir[0]] = -1
                        map[ny][nx] += 1
                        
                        max_val = max(max_val, map[ny][nx])
                        
                    else: # 합칠 수 없는 경우 이동 종료
                        break
                elif map[ny][nx] == 0:
                    break
            
    return map, max_val

# 탐색
def bfs():
    global map_2024
    queue = deque()
    ans = 0
    
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
            print(next_map, '\n\n')
    
    return ans
        
        
from math import log2
n = int(input())
map_2024 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if map_2024[i][j] != 0:
            map_2024[i][j] = int(log2(map_2024[i][j]))

print(2**bfs())


