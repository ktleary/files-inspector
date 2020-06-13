import glob
import os
from utils import getOptions


def listFiles(directory, patterns="*.*"):
    filepaths = []
    for ROOT, DIR, FILES in os.walk(directory):
        for file in FILES:
            if file.endswith((tuple(patterns))):
                filepaths.append(os.path.join(ROOT, file))
    return sorted(filepaths)


def main():
    options = getOptions(sys.argv[1:])
    files = listFiles(options.directory, options.pattern)
    for file in files:
        print(file)


if __name__ == "__main__":
    import sys
    try:
        sys.exit(main())
    except FileNotFoundError as e:
        sys.exit(e)
