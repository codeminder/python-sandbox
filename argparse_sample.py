import argparse
# https://docs.python.org/3/library/argparse.html

def parse_args():
    argParser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
    argParser.add_argument('filename')           # positional argument
    argParser.add_argument('-c', '--count')      # option that takes a value
    argParser.add_argument('-v', '--verbose',
                    action='store_true')  # on/off flag

    args = argParser.parse_args()
    return args

args = parse_args()
print(args)

