import heapq
from collections import defaultdict

INF = float('inf')

for _ in range(int(input())):
    n, m, t = map(int, input().split())

    s, g, h = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d)) # dest, dist
        graph[b].append((a, d))

    dests = [int(input()) for _ in range(t)]

    heap = [(s, 0, [s])]
    dists = [INF] * n

    while heap:
        cur_node, cur_dist, trace = heapq.heappop(heap)

        if dists[cur_node] < cur_dist:
            continue

        for next_node, next_dist in graph[cur_node]:
            if dists[next_node] > next_dist + cur_dist:
                heapq.heappush((next_node, next_dist, trace + [cur_node]))
        
