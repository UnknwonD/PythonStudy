import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())

belt = []
for _ in range(N):
    belt.append(int(input()))

check = [0 for _ in range(d+1)]
check[c] = 1
eaten = 1

# sliding window 초기화 O(k)
for i in range(k):
    cur = belt[i]
    if check[cur] == 0:
        eaten += 1
    check[cur] += 1

ans = eaten
# sliding window 업데이트 O(N)
for i in range(N): 
    start = belt[i % N]
    end = belt[(i+k) % N]
    
    check[start] -= 1
    if check[start] == 0:
        eaten -= 1
    if check[end] == 0:
        eaten += 1
    check[end] += 1

    ans = max(ans, eaten)

print(ans)