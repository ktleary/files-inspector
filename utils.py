import argparse
from constants import directoryHelp, patternHelp, reportHelp, reportLocation


# pdftotext: https://github.com/jalan/pdftotext
def pdf2text(filepath):
    import pdftotext
    with open(filepath, "rb") as f:
        pdf = pdftotext.PDF(f)
    return "\n\n".join(pdf)


def getOptions(args):
    parser = argparse.ArgumentParser(description="Parser")
    parser.add_argument("-d", "--directory", default=".", help=directoryHelp)
    parser.add_argument("-r",
                        "--report",
                        default=reportLocation,
                        help=reportHelp)
    parser.add_argument("-p",
                        "--pattern",
                        default=["*.*"],
                        action="append",
                        help=patternHelp),

    options = parser.parse_args(args)
    return options
