import argparse

parser = argparse.ArgumentParser()

# Позиционные аргументы
parser.add_argument("a", type=int, help="First argument")
parser.add_argument("b", type=int, help="Second argument")

# Опциональные аргументы

parser.add_argument("-a", "--action", help="What to do with numbers")

args = parser.parse_args()
print(args)

def summarize (a, b):
    print(a + b)

def minusize (a, b):
    print(a - b)

if args.action == 'sumarize':
    summarize(args.a, args.b)
elif args.action == 'minusuze':
    minusize(args.a, args.b)
else:
    print('You must choose action')