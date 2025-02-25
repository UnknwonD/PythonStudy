import re

total = re.findall(r'[0-9]+|[-+]+', input())

ans = 0
now = ''
for t in total:
    if now == '' and ans == 0:
        ans += int(t)
    elif t in ['+', '-']:
        if not (now == '-' and t == '+'):
            now = t
    else:
        if now == '+':
            ans += int(t)
        else:
            ans -= int(t)
print(ans)