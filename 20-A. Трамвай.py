n = int(input())

passengers = 0
max_capacity = 0

for _ in range(n):
    a, b = map(int, input().split())
    passengers = passengers - a + b
    max_capacity = max(max_capacity, passengers)

print(max_capacity)
