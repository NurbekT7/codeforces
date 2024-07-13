name = input()
name = len(set(name))
print("CHAT WITH HER!" if name % 2 == 0 else "IGNORE HIM!")