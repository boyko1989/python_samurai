import argparse

parser = argparse.ArgumentParser()

parser.add_argument("a", help="First argument", type=int)
parser.add_argument("b", help="Second argument", type=int)

parser.add_argument("-m", action="store_const", const="minusize")

args = parser.parse_args()

print(args)

def summarize (a, b):
    print(a + b)

def minusize (a, b):
    print(a - b)

if args.m == None:
    summarize(args.a, args.b)
elif args.m == 'minusize':
    minusize(args.a, args.b)
else:
    print('You must choose action')