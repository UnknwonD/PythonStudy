# Union-find
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a != b:
        if rank[a] > rank[b]:
            parent[b] = a
        elif rank[a] < rank[b]:
            parent[a] = b
        else:
            parent[b] = a
            rank[a] += 1

# 입력
n = int(input())
m = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

target = list(map(int, input().split()))

parent = [i for i in range(n)]
rank = [0 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(parent, rank, i, j)

answer = "YES"
cur = find_parent(parent, target[0]-1)

for tart in target[1:]:
    if cur == find_parent(parent, tart-1):
        continue
    else:
        answer = "NO"
        break
print(answer)