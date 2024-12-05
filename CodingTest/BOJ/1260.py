from collections import deque

def dfs(v, adj, visited):
    stack = [v]
    dfs_result = []
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            dfs_result.append(node)
            # 인접 노드를 역순으로 스택에 추가하여 작은 숫자부터 방문
            stack.extend(sorted(adj[node], reverse=True))
    
    return dfs_result

def bfs(v, adj, visited):
    queue = deque([v])
    bfs_result = []
    visited[v] = True
    
    while queue:
        node = queue.popleft()
        bfs_result.append(node)
        # 인접 노드를 정렬하여 큐에 추가하여 작은 숫자부터 방문
        for next_node in sorted(adj[node]):
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                
    return bfs_result

n, m, v = map(int, input().split())
adj = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

# DFS 수행
visited = [False] * (n + 1)
dfs_result = dfs(v, adj, visited)
print(' '.join(map(str, dfs_result)))

# BFS 수행
visited = [False] * (n + 1)
bfs_result = bfs(v, adj, visited)
print(' '.join(map(str, bfs_result)))
