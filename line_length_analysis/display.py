import matplotlib.pyplot as plt


def display_boxplot(data):
    keys = list(data.keys())
    keys.sort()
    x = []
    y = []
    for line_length in keys:
        x.append(line_length)
        y.append(data[line_length])
    plt.boxplot(x, y)
    plt.xlabel("Line Length")
    plt.ylabel("Number of Occurrences")
    plt.show()


def display_line_graph(data):
    keys = list(data.keys())
    keys.sort()
    x = []
    y = []
    for line_length in keys:
        x.append(line_length)
        y.append(data[line_length])
    plt.plot(x, y)
    plt.xlabel("Line Length")
    plt.ylabel("Number of Occurrences")
    plt.show()


def pretty_print(data):
    keys = list(data.keys())
    keys.sort()
    for line_length in keys:
        print(f"{line_length}: {data[line_length]}")
