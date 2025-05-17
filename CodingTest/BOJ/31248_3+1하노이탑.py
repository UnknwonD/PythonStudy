t = 'ABC'
def hanoi(n, start, end):
    if n == 0:
        return
    hanoi(n-1, start, 3-end-start)
    print(t[start], t[end])
    hanoi(n-1, 3-end-start, start)

n = int(input())

dp = [0, 1]
for i in range(2, 21):
    dp.append(2**(i-2) + 3 + dp[i-2])
print(dp[n])

pos = 0
while n>=2:
    hanoi(n-2, pos, 2-pos)
    print(t[pos], 'B')
    print(t[pos], 'D')
    print('B', 'D')
    
    n -= 2
    pos = 2-pos

if n == 1:
    print(t[pos], 'D')