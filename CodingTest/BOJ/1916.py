import heapq
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1) 

for _ in range(m):
    from_bus, to_bus, w = map(int, input().split())
    graph[from_bus].append((to_bus, w))

q = []
start, end = map(int, input().split())
heapq.heappush(q, (0, start))

while q:
    dist, now = heapq.heappop(q)
    
    if distance[now] < dist:
        continue
    
    for node, cost in graph[now]:
        if distance[node] > cost + dist:
            distance[node] = cost+dist
            heapq.heappush(q, (cost+dist, node))

print(distance[end])