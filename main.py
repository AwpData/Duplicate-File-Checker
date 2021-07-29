import argparse
import os
import sys

parser = argparse.ArgumentParser(description="Enter a non-empty root directory")
parser.add_argument("root", help="You must enter a root directory")

args = sys.argv
if len(args) == 1:
    print("Directory is not specified")
    exit(-1)
else:
    directory = args[1]
    os.chdir(directory)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
