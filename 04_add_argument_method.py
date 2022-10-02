import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-m", dest='B')

args = parser.parse_args()

print(args)
