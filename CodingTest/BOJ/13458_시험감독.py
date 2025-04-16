N = int(input())
A = [*map(int, input().split())]
B, C = map(int, input().split())

A.sort(reverse=True)
ans = 0

# 그리디, 감독관 큰 감독관부터 사용하면 됨.
for a in A:
    cur = a
    
    cur -= B
    ans += 1
    
    if cur < 0:
        continue
    
    ans += cur // C
    if cur % C != 0:
        ans += 1

print(ans)