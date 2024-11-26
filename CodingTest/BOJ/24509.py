### 24509

n = int(input())

total = []
answer = []

for i in range(1, n+1):
    scores = list(map(int, input().split()))
    total.append(scores)

for sub in range(1, 5):
    sorted_total = sorted(total, key=lambda x: (-x[sub], x[0]))
    
    for one in sorted_total:
        if str(one[0]) in answer:
            continue
        else:
            answer.append(str(one[0]))
            break

print(' '.join(answer))