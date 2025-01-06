import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 변수 입력
v, e = map(int, input().split())
k = int(input())
graph = {i : {} for i in range(v+1)}
distance = [INF] * (v+1)

# 간선 정보 입력 - 두 정점 사이에 여러 간선이 존재할 수 있음 (우리는 최소값만 갖고 있으면 됨)
for i in range(e):
    u, v, w = map(int, input().split())
    graph[u][v] = min(w, graph[u][v]) if v in list(graph[u].keys()) else w
    
# 다익스트라 알고리즘 시작
q = []
heapq.heappush(q, (0, k))
distance[k] = 0

while q:
    cost, now = heapq.heappop(q)
    # 이미 방문한 노드의 경우 건너띔
    if distance[now] < cost:
        continue
    
    for node, dist in graph[now].items():
        if len(distance) <= node:
            continue
        # 돌아가는 거리가 더 짧으면 거리를 갱신함
        if distance[node] > cost + dist:
            distance[node] = cost + dist
            heapq.heappush(q, (distance[node], node))

for d in distance[1:]:
    if d == INF:
        print("INF")
    else:
        print(d)
