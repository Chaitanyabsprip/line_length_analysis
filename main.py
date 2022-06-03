#! /usr/bin/env python3
import os
import sys

from line_length_analysis.args_parser import (get_output_method,
                                              get_recurse_flag,
                                              output_method_factory)
from line_length_analysis.line_length_analysis import (line_length_frequency,
                                                       lines_from_all_files,
                                                       path_of_files_from)


def main():
    args = sys.argv[1:]
    dir_arg = args[0] if len(args) > 0 else "."
    directory = os.path.abspath(dir_arg)
    files = path_of_files_from(directory, should_recurse=get_recurse_flag(args))
    lines = lines_from_all_files(files)
    output = output_method_factory(get_output_method(args))
    output(line_length_frequency(lines))


if __name__ == "__main__":
    sys.setrecursionlimit(1500)
    try:
        main()
    except RecursionError:
        print(sys.getrecursionlimit())
