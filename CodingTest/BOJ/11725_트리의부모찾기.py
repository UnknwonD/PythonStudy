import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tree = {i+1:[] for i in range(N)}

for _ in range(N-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)
    
visited = [False for _ in range(N+1)]
parent = [i for i in range(N+1)]
queue = deque()

queue.append(1)
visited[1] = True
while queue:
    now = queue.popleft()
    
    for next in tree[now]:
        if visited[next] == False:
            queue.append(next)
            parent[next] = now
            visited[next] = True
            
for p in parent[2:]:
    print(p)