import argparse

parser = argparse.ArgumentParser()

parser.add_argument("a", help="First argument", type=int)
parser.add_argument("b", help="Second argument", type=int)

parser.add_argument("-m", choices=['1', '2', '3'])

args = parser.parse_args()

print(args)

def summarize (a, b):
    print(a + b)

def minusize (a, b):
    print(a - b)

if args.m == False:
    summarize(args.a, args.b)
elif args.m == True:
    minusize(args.a, args.b)