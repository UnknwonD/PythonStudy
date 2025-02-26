def dfs(n, value, nr, nc): 
    if n == 0:
        return value  # 최종적으로 값 반환
    
    half = 2 ** (n-1)  # 절반 크기
    
    if nr < half and nc < half:  # 1사분면
        plane = 0
    elif nr < half and nc >= half:  # 2사분면
        plane = 1
        nc -= half
    elif nr >= half and nc < half:  # 3사분면
        plane = 2
        nr -= half
    else:  # 4사분면
        plane = 3
        nr -= half
        nc -= half
    
    return dfs(n-1, value + (half * half) * plane, nr, nc)

n, r, c = map(int, input().split())  # 크기, 행, 열
print(dfs(n, 0, r, c))
