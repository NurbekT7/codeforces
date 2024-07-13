rock, color = int(input()), list(input())

count = 0
table = []

for i in color:
    if table and table[-1] == i:
        count += 1
    else:
        table.append(i)

print(count)