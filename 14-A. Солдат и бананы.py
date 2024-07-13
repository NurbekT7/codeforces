k, n, w = map(int, input().split())

sum = 0

for i in range(1, w+1):
    sum += k * i

print(max(0, sum - n))