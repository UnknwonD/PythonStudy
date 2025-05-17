N, d, k, c = map(int, input().split())
total = []
max_ans = 0

for _ in range(N):
    total.append(int(input()))

check = [0 for _ in range(d+1)]
ans = 1
check[c] += 1

for i in range(k):
    cur = total[i % N]
    if not check[cur]:
        ans += 1
    check[cur] += 1
max_ans = ans

for i in range(N):
    start = total[(i) % N] # 뺄 것
    end = total[(i + k) % N] # 추가할 것

    check[start] -= 1
    if check[start] == 0:
        ans -= 1

    if check[end] == 0:
        ans += 1
    check[end] += 1

    max_ans = max(ans, max_ans)

print(max_ans)