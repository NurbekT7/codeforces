import sys


def custom_print(*args, sep=' ', end='\n', file=sys.stdout):
    output = sep.join(map(str, args))
    file.write(output + end)


a = input()
custom_print(a)
