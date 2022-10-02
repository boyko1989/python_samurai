import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--action", action="store")

args = parser.parse_args()

print(args)