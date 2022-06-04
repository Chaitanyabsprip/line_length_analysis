import argparse
from abc import ABC, abstractmethod


class ArgsParser(ABC):
    @abstractmethod
    def get_recurse_flag(self):
        pass

    @abstractmethod
    def get_display_method(self):
        pass

    @abstractmethod
    def get_file_paths(self):
        pass


class ArgsParserImpl(ArgsParser):
    def __init__(self, parser: argparse.ArgumentParser):
        ArgsParserImpl.initialise_parser(parser)
        self._args = parser.parse_args()

    @staticmethod
    def initialise_parser(parser):
        parser.add_argument("-r", "--recurse", action="store_true")
        parser.add_argument(
            "-d",
            "--display",
            choices=["line", "box", "stdout"],
            default="stdout",
        )
        parser.add_argument("file_paths", nargs="+")

    def get_recurse_flag(self):
        return self._args.recurse

    def get_display_method(self):
        return self._args.display

    def get_file_paths(self):
        return self._args.file_paths
