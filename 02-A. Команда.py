n = int(input())
out = 0

for _ in range(n):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        out += 1

print(out)