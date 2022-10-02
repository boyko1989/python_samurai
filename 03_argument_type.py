import argparse

parser = argparse.ArgumentParser()

# Позиционные аргументы
parser.add_argument("a", type=int, help="First argument")
parser.add_argument("b", type=int, help="Second argument")

args = parser.parse_args()
print(args)

def summarize (a, b):
    print(a + b)

summarize(args.a, args.b)