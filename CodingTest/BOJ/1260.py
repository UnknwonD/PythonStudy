from collections import deque

n, m, v = map(int, input().split())

adj = {i:[] for i in range(1, n+1)}

for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

print(adj)
for val in adj.values():
    sorted(val)
print(adj)

stack = []
visited = [0 for _ in range(n + 1)]
queue = deque()

# DFS
dfs_visited = []
stack.append(v)
while stack:
    now = stack.pop()
    dfs_visited.append(now)
    visited[now] = 1
    
    for next_node in adj[now]:
        if next_node not in dfs_visited and visited[now] != 1:
            print(next_node, dfs_visited)
            stack.append(next_node)
            visited[next_node] = 1

print(' '.join([str(node) for node in dfs_visited]))

# BFS
bfs_visited = []
queue.append(v)
while queue:
    cur = queue.popleft()
    bfs_visited.append(cur)
    
    for next_node in adj[cur]:
        if next_node not in bfs_visited and next_node not in queue:
            queue.append(next_node)

print(' '.join([str(node) for node in bfs_visited]))