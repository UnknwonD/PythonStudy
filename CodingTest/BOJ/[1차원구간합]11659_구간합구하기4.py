import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = [0] + list(map(int, input().split()))

# 구간합 배열 생성
data_sum = [data[1]]
for i in range(1, len(data)):
    data_sum.append(data_sum[i-1] + data[i])

# 입력 받기
for _ in range(M):
    s, e = map(int, input().split())
    print(data_sum[e] - data_sum[s-1])