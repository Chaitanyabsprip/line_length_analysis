import os


def line_length_frequency(lines):
    frequency_map = {}
    while len(lines) > 0:
        string = lines.pop()
        if isinstance(string, str):
            string_frequency = frequency_map.get(len(string), 0)
            frequency_map[len(string)] = string_frequency + 1
    return frequency_map


def file_lines(filename):
    try:
        with open(filename, mode="r", encoding="UTF-8") as file:
            return list(filter(lambda x: x != "\n", file.readlines()))
    except FileNotFoundError:
        return []
    except UnicodeDecodeError:
        print(f"{filename} is not a valid UTF-8 file")
        return []


def lines_from_all_files(files, lines=None):
    lines = lines or []
    if len(files) == 0:
        return lines
    lines = lines + file_lines(files.pop())
    return lines_from_all_files(files, lines)


def path_of_files_in_directory(directory, should_recurse=False):
    list_of_file_paths = []
    for file in os.scandir(directory):
        if file.is_file():
            list_of_file_paths.append(absolute_path_of_file(file.path))
        elif should_recurse:
            list_of_file_paths = (
                list_of_file_paths
                + path_of_files_in_directory(
                    file.path, should_recurse=should_recurse
                )
            )
    return list_of_file_paths


def absolute_path_of_file(filename):
    absolute_path = os.path.abspath(filename)
    return absolute_path
