n = int(input())

data = []
for i in range(n):
    word = input()
    if word not in data:
        data.append(word)

print(sorted(data, key=lambda x: (len(x), x)))