lst = []
for i in range(5):
    lst.append(list(map(int, input().split())))

for i in range(5):
    for j in range(5):
        if lst[i][j] == 1:
            print(abs(2-i) + abs(2-j))
