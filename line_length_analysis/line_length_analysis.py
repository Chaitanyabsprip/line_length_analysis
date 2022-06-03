import os


def line_length_frequency(lines):
    frequency_map = {}
    while len(lines) > 0:
        string = lines.pop()
        if isinstance(string, str):
            string_frequency = frequency_map.get(len(string), 0)
            frequency_map[len(string)] = string_frequency + 1
    return frequency_map


def lines_from_all_files(files, lines=None):
    lines = lines or []
    if len(files) == 0:
        return lines
    lines = lines + _file_lines(files.pop())
    return lines_from_all_files(files, lines)


def _file_lines(filename):
    try:
        with open(filename, mode="r", encoding="UTF-8") as file:
            return list(filter(lambda x: x != "\n", file.readlines()))
    except FileNotFoundError:
        return []
    except UnicodeDecodeError:
        print(f"{filename} is not a valid UTF-8 file")
        return []


def path_of_files_from(path, should_recurse=False):
    if os.path.isdir(path):
        return _path_of_files_in(path, should_recurse)
    if os.path.isfile(path):
        return [path]
    return []


def _path_of_files_in(directory, should_recurse=False):
    file_paths = []
    for file in os.scandir(directory):
        if file.is_file():
            file_paths.append(_absolute_path_of(file.path))
        elif should_recurse:
            file_paths = file_paths + path_of_files_from(
                file.path, should_recurse
            )
    return file_paths


def _absolute_path_of(filename):
    absolute_path = os.path.abspath(filename)
    return absolute_path
