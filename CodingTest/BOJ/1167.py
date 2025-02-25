# 두 점 사이의 거리가 가장 긴 것을 찾아내야됨 (2번의 dfs 수행)
def dfs(start, adj, visited):
    stack = [(start, 0)]
    while stack:
        node, dist = stack.pop() # 노드와 거리
        
        for next_node, new_dist in adj[node].items():
            if not visited[next_node]:
                stack.append((next_node, new_dist + dist))
                distance[next_node] = new_dist + dist
                visited[next_node] = True
    return distance

v = int(input())
graph = [{} for _ in range(v+1)]

for _ in range(v):
    tmp = list(map(int, input().split()))
    
    for i in range(1, len(tmp)-1, 2):
        graph[tmp[0]][tmp[i]] = tmp[i+1]
    

target = 1
for _ in range(2):
    visited = [False for _ in range(v+1)]
    distance = [-1 for _ in range(v+1)]
    
    ans = dfs(target, graph, visited)
    ans[target] = -1
    target = ans.index(max(ans))

print(max(ans))