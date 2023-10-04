from abc import ABC, abstractmethod
from math import ceil

import matplotlib.pyplot as mplt
import plotext as plt

from line_length_analysis.line_length_analysis import Analysis


class Display(ABC):
    @abstractmethod
    def plot(self, analyses: list[Analysis]) -> None:
        raise NotImplementedError


class DisplayFactory(ABC):
    @abstractmethod
    def create_display(self, method: str) -> Display:
        pass


def display_method_factory(method: str) -> Display:
    if method == "box":
        return Boxplot()
    if method == "line":
        return LineGraph()
    if method == "line-cli":
        return LineGraphCLI()
    return PrettyPrint()


class Boxplot(Display):
    def plot(self, analyses: list[Analysis]):
        x, y = _sanitize(analyses)
        mplt.boxplot(x, y)
        mplt.ylabel("Line Length")
        mplt.xticks(
            list(range(len(analyses) + 1)),
            [""] + [analysis.title for analysis in analyses],
        )
        mplt.show()


class LineGraph(Display):
    def plot(self, analyses: list[Analysis]):
        num_of_analyses = len(analyses)
        num_of_rows, num_of_cols = get_subplot_dimension(num_of_analyses)
        _, axes = mplt.subplots(num_of_rows, num_of_cols)
        for row in range(num_of_rows):
            for col in range(num_of_cols):
                index = row * num_of_cols + col
                x, y = _sanitize_analysis(analyses[index].line_length_analysis)
                if num_of_analyses == 1:
                    graph = axes
                else:
                    graph = axes[col]
                if num_of_cols > 1:
                    graph = axes[row, col]
                graph.plot(x, y)
                graph.set_title(analyses[index].title)
                graph.set_xlabel("Line Length")
                graph.set_ylabel("Number of Occurrences")
        mplt.show()


def get_subplot_dimension(num_of_plots):
    modtwo = num_of_plots % 2
    num_of_rows = ceil(num_of_plots / 2) + modtwo
    if num_of_plots == 1:
        num_of_rows = 1
    num_of_cols = 2 - modtwo
    return num_of_rows, num_of_cols


class LineGraphCLI(Display):
    def plot(self, analyses: list[Analysis]):
        plt.theme("pro")
        plt.limit_size(False, False)
        plt.plot_size(140, 36)
        fig = plt.subplots(len(analyses), 1)
        for idx, analysis in enumerate(analyses):
            x, y = _sanitize_analysis(analysis.line_length_analysis)
            graph = fig.subplot(idx + 1, 1)
            graph.plot(x, y)
            graph.xlabel("Line Length")
            graph.ylabel("Number of Occurrences")
        plt.show()


class PrettyPrint(Display):
    def plot(self, analyses):
        for analysis in analyses:
            data = analysis.line_length_analysis
            keys = list(data.keys())
            keys.sort()
            print(analysis.title, end=" = {")
            for line_length in keys:
                print(f"{line_length}: {data[line_length]}", end=", ")
            print("}\n")


def _sanitize(analyses):
    x, y = [], []
    for data in analyses:
        x_temp, y_temp = _sanitize_analysis(data.line_length_analysis)
        x.append(x_temp)
        y.append(y_temp)
    return x, y


def _sanitize_analysis(data):
    keys = list(data.keys())
    keys.sort()
    x = []
    y = []
    for line_length in keys:
        x.append(line_length)
        y.append(data[line_length])
    return x, y
