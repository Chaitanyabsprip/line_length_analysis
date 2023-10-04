#! /usr/bin/env python3
import argparse
import sys

from line_length_analysis.args_parser import ArgsParser, ArgsParserImpl
from line_length_analysis.config import Config
from line_length_analysis.display import Display, display_method_factory
from line_length_analysis.line_length_analysis import \
    get_line_length_frequency_for_each


def main():
    parser = argparse.ArgumentParser(
        description="Analyze the length of lines of source file(s)."
    )
    args_parser: ArgsParser = ArgsParserImpl(parser)
    config: Config = args_parser.get_config()
    analyses = get_line_length_frequency_for_each(
        config.file_paths, config.should_recurse
    )
    display: Display = display_method_factory(config.display_method)
    display.plot(analyses)


if __name__ == "__main__":
    sys.setrecursionlimit(15000)
    try:
        main()
    except RecursionError:
        print(sys.getrecursionlimit())
