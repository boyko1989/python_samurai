import sys

print(sys.argv)

a = int(sys.argv[1])
b = int(sys.argv[2])


def summarize(a, b):
    return a + b


print(summarize(a, b))
