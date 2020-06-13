import argparse
from constants import directoryHelp, patternHelp, reportHelp


def getOptions(args):
    parser = argparse.ArgumentParser(description="Parser")
    parser.add_argument("-d", "--directory", default=".", help=directoryHelp)
    parser.add_argument("-r",
                        "--report",
                        default="/tmp/report.md",
                        help=reportHelp)
    parser.add_argument("-p", "--pattern", action="append", help=patternHelp),

    options = parser.parse_args(args)
    return options
