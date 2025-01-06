import heapq

INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    reverse_graph[e].append((s, w))

def dijkstra(start, reverse=False):
    root = graph if not reverse else reverse_graph
    distance = [INF] * (n+1)
    
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)        
        if distance[now] < dist:
            continue
        for node, cost in root[now]:
            ndist = cost + dist
            if distance[node] > ndist: 
                distance[node] = ndist
                heapq.heappush(q, (ndist, node))
                
    return distance[1:]

to_x = dijkstra(x)
from_x = dijkstra(x, True)

print(max([x1 + x2 for x1, x2 in zip(to_x, from_x)]))