n = int(input())
text = ""

for _ in range(n):
    word = input()
    if len(word) <= 10:
        text += f"{word}\n"
    else:
        text += f"{word[0]}{len(word)-2}{word[-1]}\n"

print(text)
