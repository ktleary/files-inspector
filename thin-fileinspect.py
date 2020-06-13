import os
from utils import getOptions, pdf2text


def listFiles(directory, patterns="*.*"):
    filepaths = []
    for ROOT, DIR, FILES in os.walk(directory):
        for file in FILES:
            if file.endswith((tuple(patterns))):
                filepaths.append(os.path.join(ROOT, file))
    return sorted(filepaths)


def processFiles(filelist):
    for filepath in filelist:
        if filepath.endswith("pdf"):
            print(filepath)
            text = pdf2text(filepath)
    return text


def main():
    options = getOptions(sys.argv[1:])
    files = listFiles(options.directory, options.pattern)
    processFiles(files)


if __name__ == "__main__":
    import sys
    try:
        sys.exit(main())
    except FileNotFoundError as e:
        sys.exit(e)
