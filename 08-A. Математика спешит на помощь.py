lst = list(map(int, input().split("+")))

lst.sort()

out = ""

for i in lst:
    out += f"{i}+"

print(out[:-1])