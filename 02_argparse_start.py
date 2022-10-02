import argparse

# объект класса ArgumentParser (часть модуля argparse)
parser = argparse.ArgumentParser()

parser.add_argument("test")

args = parser.parse_args()

print(args)
