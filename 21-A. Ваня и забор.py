n, h = map(int, input().split())
heights = list(map(int, input().split()))

min_width = sum(1 if height <= h else 2 for height in heights)

print(min_width)
