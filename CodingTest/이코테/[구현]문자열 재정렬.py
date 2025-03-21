data = list(input())
data.sort()
answer = ''
total_sum = 0
for d in data:
    try:
        total_sum += int(d)
    except:
        answer += d

print(f"{answer}{total_sum}")