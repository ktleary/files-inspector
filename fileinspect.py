"""

Loop through a direcotry obtain file metadata

"""
import glob
import os.path
from pyexiftool import exiftool


def process_files(filepaths):
    metadata = []

    for filepath in filepaths:
        basename = os.path.basename(filepath)
        filename, ext = os.path.splitext(basename)

        with exiftool.ExifTool() as et:
            print(str(filepath))
            metadata = et.get_metadata(filepath)
            for d in metadata:
                print(metadata.get(d))

    return metadata


def list_files(notes_dir, pattern="*.*"):
    """
    List files in a directory

    Parameters
    ----------
    journal_dir : str
        Path to the directory containing the files
    pattern: str
        Patterns matching files. The default is '*.*' If there are multiple patterns, separate them with a |, such as '*.pdf|*.md'

    """

    filepaths = []

    for patt in pattern.split("|"):
        filepaths.extend(glob.glob(os.path.join(notes_dir, patt)))
    return sorted(filepaths)


def parse_args(args=None):
    from argparse import ArgumentParser

    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "--files-dir", default=".", help="path to folder containing unprocessed items. [.]"
    )
    parser.add_argument(
        "--pattern",
        action="append",
        help=(
            "pattern to match files. You can repeat this argument to"
            " match multiple file types. [*.*]"
        ),
    )
    parser.add_argument(
        "--output",
        default="report",
        help="name of output file. [report]",
    )

    parser.add_argument("journal_dir", nargs="*", help="journal file paths.")
    args = parser.parse_args(args=args)

    # Use the list of files the user specify, otherwise, fall back to listing
    # a directory.
    if not args.journal_dir:
        if args.pattern is None:
            args.pattern = ["*.*"]
        patterns = "|".join(args.pattern)
        args.journal_dir = list_files(args.files_dir, pattern=patterns)
    return args


def main(args=None):
    args = parse_args(args)

    filesinfo = process_files(args.journal_dir)


if __name__ == "__main__":
    import sys

    try:
        sys.exit(main())
    except FileNotFoundError as e:
        # Failed either because it didn't find any files or because Graphviz
        # wasn't installed
        sys.exit(e)


"""
References:
1. PyExifTool – A Python wrapper for Phil Harvey’s ExifTool: https://smarnach.github.io/pyexiftool/

"""
