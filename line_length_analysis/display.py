from math import ceil

import matplotlib.pyplot as plt


def display_boxplot(analyses):
    x, y = _sanitize(analyses)
    plt.boxplot(x, y)
    plt.xlabel("Line Length")
    plt.xticks(
        list(range(len(analyses) + 1)),
        [""] + [analysis.title for analysis in analyses],
    )
    plt.show()


def _sanitize(analyses):
    x, y = [], []
    for data in analyses:
        x_temp, y_temp = _sanitize_analysis(data.line_length_analysis)
        x.append(x_temp)
        y.append(y_temp)
    return x, y


def display_line_graph(analyses):
    modtwo = len(analyses) % 2
    num_of_rows = ceil(len(analyses) / 2) + modtwo
    num_of_cols = 2 - modtwo
    print(f"{num_of_rows} rows, {num_of_cols} columns")
    _, axes = plt.subplots(num_of_rows, num_of_cols)
    for row in range(num_of_rows):
        for col in range(num_of_cols):
            index = row * num_of_cols + col
            x, y = _sanitize_analysis(analyses[index].line_length_analysis)
            graph = axes[col]
            if num_of_cols > 1:
                graph = axes[row, col]
            graph.plot(x, y)
            graph.set_title(analyses[index].title)
            graph.set_xlabel("Line Length")
            graph.set_ylabel("Number of Occurrences")
    # x, y = _sanitize_analysis(analyses)
    # plt.plot(x, y)
    plt.show()


def pretty_print(analyses):
    for analysis in analyses:
        data = analysis.line_length_analysis
        keys = list(data.keys())
        keys.sort()
        print(analysis.title, end=" = {")
        for line_length in keys:
            print(f"{line_length}: {data[line_length]}", end=", ")
        print("}\n")


def _sanitize_analysis(data):
    keys = list(data.keys())
    keys.sort()
    x = []
    y = []
    for line_length in keys:
        x.append(line_length)
        y.append(data[line_length])
    return x, y


def display_method_factory(method_name):
    if method_name == "box":
        return display_boxplot
    if method_name == "line":
        return display_line_graph
    return pretty_print
