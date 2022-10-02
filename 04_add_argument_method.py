import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--action", action="store_const", const="value")

args = parser.parse_args()

print(args)