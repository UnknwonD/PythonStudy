def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x

N, M = map(int, input().split())
temp = list(map(int, input().split()))
truth = temp[1:]  # 진실을 아는 사람들

parent = [i for i in range(N + 1)]
parties = []

for _ in range(M):
    party = list(map(int, input().split()))[1:]
    parties.append(party)
    for i in range(1, len(party)):
        union(party[0], party[i])

# 진실을 아는 사람들의 root 그룹을 구함
truth_root = set(find(x) for x in truth)
# print(truth_root)

ans = 0
for party in parties:
    roots = set(find(x) for x in party)
    if roots.isdisjoint(truth_root):
        ans += 1

print(ans)
