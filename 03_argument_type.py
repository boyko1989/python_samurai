import argparse

parser = argparse.ArgumentParser()

# Позиционные аргументы
parser.add_argument("a")
parser.add_argument("b")

args = parser.parse_args()
print(args)

def summarize (a, b):
    print(a + b)