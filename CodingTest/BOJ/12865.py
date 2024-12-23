n, k = map(int, input().split())

products = []

for _ in range(n):
    products.append(list(map(int, input().split())))
    
# 0 : weight | 1 : value
products.sort(key = lambda x: (x[0], -x[1]))

dp = [[0 for _ in range(k+1)] for _ in range(n)]

# 첫번째 물건을 기준으로 먼저 초기화
for w in range(len(dp[0])):
    if w >= products[0][0]:
        dp[0][w] = products[0][1]

# 수정 : 한 물건을 여러개 넣는 게 아니라, 넣거나 안넣거나 밖에 없음
# 따라서 넣은 것과 안넣은 것의 결과값을 비교하면됨        
for i in range(1, len(dp)):
    for w in range(len(dp[0])):
        if w-products[i][0] >= 0:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-products[i][0]] + products[i][1])
        else:
            dp[i][w] = dp[i-1][w]

print(dp[-1][-1])