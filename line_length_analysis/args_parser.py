import sys

from line_length_analysis.display import (display_boxplot, display_line_graph,
                                          pretty_print)


def get_recurse_flag(args):
    return "-r" in args


def get_output_method(args):
    if "-o" in args:
        return _extract_output_method_or_fail(args)
    return "stdout"


def _extract_output_method_or_fail(args):
    try:
        return _get_output_method_arg(args)
    except IndexError:
        return _safely_exit_with("output method", 1)


def _get_output_method_arg(args):
    value_index = args.index("-o")
    return args[value_index + 1]


def _safely_exit_with(message, exit_code):
    print("Error: Please provide an ", message)
    sys.exit(exit_code)


def output_method_factory(method_name):
    if method_name == "box":
        return display_boxplot
    if method_name == "line":
        return display_line_graph
    return pretty_print
