# RGB 거리
# https://www.acmicpc.net/problem/1149

def memo(cur, color):
    # print(color, cur, len(dp), len(dp[0]))
    if dp[color][cur] != -1:
        return dp[color][cur]
    
    if color == 0: # R
        target_color = (1, 2)
    elif color == 1: # G
        target_color = (0, 2)
    else: # B
        target_color = (0, 1)
    
    if cur+1 < len(dp[0]):
        dp[color][cur] = min(memo(cur+1, target_color[0])+total_price[cur][color], memo(cur+1, target_color[1])+total_price[cur][color])
    
    return dp[color][cur]


n = int(input())

total_price = []
dp = [[-1 for _ in range(n)] for _ in range(3)]

for i in range(n):
    total_price.append(list(map(int, input().split())))

for i in range(3):
    dp[i][-1] = total_price[-1][i]
    
print(min([memo(0, 0), memo(0, 1), memo(0, 2)]))