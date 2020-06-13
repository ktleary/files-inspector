import glob
import os
from utils import getOptions


def listFiles(directory, patterns="*.*"):
    filepaths = []
    for pattern in patterns.split("|"):
        filepaths.extend(glob.glob(os.path.join(directory, pattern)))
    return sorted(filepaths)


def main():
    args = getOptions(sys.argv[1:])
    # files = listFiles(args.directory, args.patterns)
    # print(files)
    print({
        "direct": args.directory,
        "report": args.report,
        "patterns": args.patterns
    })


if __name__ == "__main__":
    import sys
    try:
        sys.exit(main())
    except FileNotFoundError as e:
        sys.exit(e)
