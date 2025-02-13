# https://www.acmicpc.net/problem/1717
# 집합의 연산

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, rank, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a != b:
        if rank[a] > rank[b]:  # 더 깊은 트리에 붙이기
            parent[b] = a
        elif rank[a] < rank[b]:
            parent[a] = b
        else:
            parent[b] = a
            rank[a] += 1  # 같은 높이면 한쪽을 증가

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
rank = [0] * (n+1)  # 트리 높이를 저장하는 배열

for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 1:  # 같은 집합인지 확인
        print("YES" if find_parent(parent, a) == find_parent(parent, b) else "NO")
    else:  # 합집합 연산
        union_parent(parent, rank, a, b)