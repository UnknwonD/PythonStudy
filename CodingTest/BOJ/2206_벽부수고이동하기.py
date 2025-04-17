from collections import deque

N, M = map(int, input().split())
board = [[*map(int, list(input()))] for _ in range(N)]

q = deque()

# 벽을 부쉈는지, 안부섰는지 저장해야됨
# 이동하는 방식 중, 벽을 부쉈을 때와 지금 중, 더 짧게 이동할 수 있는지 비교해야됨

# 1. 벽 너머부터 N, M까지의 이동거리 계산