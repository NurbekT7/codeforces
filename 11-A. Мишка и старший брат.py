l, b = map(float, input().split())
year = 0

while l < b or l == b:
    l *= 3
    b *= 2
    year += 1

print(year)