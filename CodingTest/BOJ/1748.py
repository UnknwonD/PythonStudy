def count_digits(N):
    digits = 0
    length = 1
    start = 1

    while start <= N:
        end = min(start * 10 - 1, N)
        count = end - start + 1
        digits += count * length
        length += 1
        start *= 10

    return digits

N = int(input())

print(count_digits(N))
