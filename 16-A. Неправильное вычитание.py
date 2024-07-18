n, c = map(int, input().split())

for i in range(1, c+1):
    if str(n)[-1] != "0":
        n -= 1
    else:
        n //= 10
print(n)