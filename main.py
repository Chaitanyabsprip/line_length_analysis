#! /usr/bin/env python3
import argparse
import sys

from line_length_analysis.args_parser import ArgsParser, ArgsParserImpl
from line_length_analysis.display import display_method_factory
from line_length_analysis.line_length_analysis import \
    get_line_length_frequency_for_each


def main():
    parser = argparse.ArgumentParser(
        description="Analyze the length of lines of source file(s)."
    )
    args_parser: ArgsParser = ArgsParserImpl(parser)
    should_recurse = args_parser.get_recurse_flag()
    file_paths = args_parser.get_file_paths()
    display_method = args_parser.get_display_method()
    print(should_recurse)
    print(file_paths)
    print(display_method)
    analyses = get_line_length_frequency_for_each(file_paths)
    output = display_method_factory(display_method)
    output(analyses)


if __name__ == "__main__":
    sys.setrecursionlimit(1500)
    try:
        main()
    except RecursionError:
        print(sys.getrecursionlimit())
