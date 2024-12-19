
n, k = map(int, input().split())
products = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(k)] # 무게만큼 연결해주기