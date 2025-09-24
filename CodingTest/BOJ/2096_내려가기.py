import sys

input = sys.stdin.readline()
n = int(input())

steps = [[*map(int, input().split())] for _ in range(n)]

dp = [[0]*n for _ in range(n)]

for i in range(n):
    dp[-1][i]
