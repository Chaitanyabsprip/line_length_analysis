import argparse
from abc import ABC, abstractmethod

from line_length_analysis.config import Config


class ArgsParser(ABC):
    @abstractmethod
    def get_config(self) -> Config:
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
            choices=["line", "box", "stdout", "line-cli"],
            default="stdout",
        )
        parser.add_argument("file_paths", nargs="+")

    def get_config(self) -> Config:
        return Config(
            self._args.recurse, self._args.display, self._args.file_paths
        )
