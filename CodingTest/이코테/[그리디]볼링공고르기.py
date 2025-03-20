n, m = map(int, input().split())
K = list(map(int, input().split()))

array = [0] * 11

for x in K:
    array[x] += 1

res = 0
for i in range(1, m+1):
    n -= array[i] # 무게가 i인 볼링공의 개수 (A가 선택할 수 있는 개수 제외)
    res += array[i] * n

print(res)