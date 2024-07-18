n = int(input())
results = input()

anton = results.count("A")
danik = results.count("D")

print("Friendship" if anton == danik else "Anton" if anton > danik else "Danik")