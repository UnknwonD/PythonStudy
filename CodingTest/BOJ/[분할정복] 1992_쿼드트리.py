n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]

def bfs(n, nr, nc):
    # 현재 영역이 모두 같은 값인지 확인
    first = graph[nr][nc]
    all_same = True

    for i in range(nr, nr + n):
        for j in range(nc, nc + n):
            if graph[i][j] != first:
                all_same = False
                break
        if not all_same:
            break

    # 만약 영역 내 모든 값이 같다면 해당 값 반환
    if all_same:
        return str(first)

    # 4개 영역으로 분할하여 탐색
    half = n // 2
    ans_1 = bfs(half, nr, nc)       # 좌상단
    ans_2 = bfs(half, nr, nc + half) # 우상단
    ans_3 = bfs(half, nr + half, nc) # 좌하단
    ans_4 = bfs(half, nr + half, nc + half) # 우하단

    return f'({ans_1}{ans_2}{ans_3}{ans_4})'

print(bfs(n, 0, 0))
