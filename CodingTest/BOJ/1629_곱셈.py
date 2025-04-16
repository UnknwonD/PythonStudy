# 코드를 다시 돌려본다면, 이 문제는 모듈러 지수 분할정복 법칙이 있음.

def power(a, b, c):
    if b == 0:
        return 1
    if b == 1:
        return a % c
    
    half = power(a, b // 2, c)
    
    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c

A, B, C = map(int, input().split())
print(power(A, B, C))