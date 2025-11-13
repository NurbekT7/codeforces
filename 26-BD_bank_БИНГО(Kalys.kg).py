lst = list(map(int, input().split()))
if len(set(lst)) == 1:
    print("BINGO")
else:
    lst.sort()
    print(*lst)