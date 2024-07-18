n = int(input())
x = 0

for _ in range(n):
    op = input()
    if "X" in op:
        if "++" in op:
            x += 1
        elif "--" in op:
            x -= 1

print(x)