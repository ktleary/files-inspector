import argparse
from constants import directoryHelp, patternHelp, reportHelp, reportLocation


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
