def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, rank, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a != b:
        if rank[a] > rank[b]:
            parent[b] = a
        elif rank[a] < rank[b]:
            parent[a] = b
        else:
            parent[a] = b
        
n = int(input())
m = int(input())
rank = [1 for _ in range(n+1)]
parent = [i for i in range(n+1)]

for i in range(1, n+1):
    conn = list(map(int, input().split()))
    
    for j in range(len(conn)):
        if conn[j] == 1:
            union_parent(parent, rank, i, j)

route = list(map(int, input().split()))
now = find_parent(parent, route[0])

for r in range(1, len(route)):
    target = find_parent(parent, route[r])
    
    if now != target:
        now = -1
        break

print(parent)
if now == -1:
    print("NO")
else:
    print("YES")