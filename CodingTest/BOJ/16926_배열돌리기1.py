N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

layers = min(N, M) // 2

for layer in range(layers):
    elements = []

    # 상단
    for i in range(layer, M - layer):
        elements.append(arr[layer][i])
    # 우측
    for i in range(layer + 1, N - layer - 1):
        elements.append(arr[i][M - layer - 1])
    # 하단
    for i in range(M - layer - 1, layer - 1, -1):
        elements.append(arr[N - layer - 1][i])
    # 좌측
    for i in range(N - layer - 2, layer, -1):
        elements.append(arr[i][layer])

    # 회전
    rot = R % len(elements)
    elements = elements[rot:] + elements[:rot]

    idx = 0
    # 상단
    for i in range(layer, M - layer):
        arr[layer][i] = elements[idx]
        idx += 1
    # 우측
    for i in range(layer + 1, N - layer - 1):
        arr[i][M - layer - 1] = elements[idx]
        idx += 1
    # 하단
    for i in range(M - layer - 1, layer - 1, -1):
        arr[N - layer - 1][i] = elements[idx]
        idx += 1
    # 좌측
    for i in range(N - layer - 2, layer, -1):
        arr[i][layer] = elements[idx]
        idx += 1

for row in arr:
    print(' '.join(map(str, row)))
