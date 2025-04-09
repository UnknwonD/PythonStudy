from collections import deque

# 이동 처리 - 같은 숫자 만나면 결합시켜주기
# 한 번 이동에는 한 번의 결합만 가능함
def move():
    ...

# 탐색
def bfs():
    global map
    queue = deque()


n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]