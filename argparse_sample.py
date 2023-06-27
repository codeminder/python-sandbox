import argparse
# https://docs.python.org/3/library/argparse.html

argParser = argparse.ArgumentParser()
argParser.add_argument("-n", "--name", help="your name")
argParser.add_argument("-d", "--default", help="arg with default value", default="A def value")

args = argParser.parse_args()
print("args=%s" % args)

print("args.name=%s" % args.name)
print("args.name=%s" % args.name)