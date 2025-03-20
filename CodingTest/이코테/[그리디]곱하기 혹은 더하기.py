import sys

numbers = sys.stdin.readline().replace('\n','')

cur = 0
for num in numbers:
    now = int(num)
    if cur + now > cur * now:
        cur += now
    else:
        cur *= now

print(cur)