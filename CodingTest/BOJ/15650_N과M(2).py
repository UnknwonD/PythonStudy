from itertools import combinations

n, m = map(int, input().split())
total = [i+1 for i in range(n)]

answer = []

for data in combinations(total, m):
    target = sorted(data)
    if target not in answer:
        answer.append(target)
    
for ans in answer:
    for a in ans:
        print(a, end=' ')
    print('')

