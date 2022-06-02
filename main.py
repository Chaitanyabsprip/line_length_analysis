#! /usr/bin/env python3
import os
import sys

from line_length_analysis.display import display_boxplot
from line_length_analysis.line_length_analysis import (
    line_length_frequency, lines_from_all_files, path_of_files_in_directory)


def main():
    dir_arg = sys.argv[1] if len(sys.argv) > 1 else "."
    directory = os.path.abspath(dir_arg)
    files = path_of_files_in_directory(directory, should_recurse=True)
    lines = lines_from_all_files(files)
    display_boxplot(line_length_frequency(lines))


if __name__ == "__main__":
    sys.setrecursionlimit(1500)
    try:
        main()
    except RecursionError:
        print(sys.getrecursionlimit())
