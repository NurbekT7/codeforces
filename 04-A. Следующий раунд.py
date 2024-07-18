n, k = map(int, input().split())
list = list(map(int, input().split()))

k = list[k - 1]

out = 0

for i in list:
    if i >= k and i > 0:
        out += 1

print(out)