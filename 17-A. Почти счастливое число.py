n = int(input())

count = 0
for i in str(n):
    if i == '4' or i == '7':
        count += 1

count_str = str(count)
is_almost_lucky = all(c in '47' for c in count_str)

if is_almost_lucky:
    print("YES")
else:
    print("NO")
