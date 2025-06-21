# 0 - 14층, 1 - 14호까지 있음
# 0층은 호수만큼 존재함
# 1층은 0층의 1호 ~ b호까지의 수 합산만큼 살고 있음
# 2층은 1층의 1호 ~ b호까지의 수 합산만큼 살고 있음

for _ in range(int(input())):
    k = int(input())
    n = int(input())
    f0 = [i for i in range(1, n+1)]
    
    for f in range(k):
        for num in range(1, n):
            f0[num] += f0[num-1]
    print(f0[-1])
    