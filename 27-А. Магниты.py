n = int(input())
island = 1
before = 0
for _ in range(n):
    a = int(input())

    # будем проверять кол-во цикла, если 1 то вместо {before = 0} оставим настоящий
    if _ == 0:
        before = a
        continue

    if before == a:
        before = a
        continue
    before = a
    island += 1

print(island)