import sys

n = int(sys.stdin.readline())
money = list(map(int, sys.stdin.readline().split()))
money.sort()

target = 1
for x in money:
    if target < x:
        break
    target += x

print(target)