from collections import namedtuple

point = namedtuple("point", "line column")
engine = namedtuple("engine", "star first second")
DEBUG = True


def find_stars(data: list[str]) -> list[point]:
    result = []
    for (line_no, line) in enumerate(data):
        result.extend([point(line_no, col_no) for col_no, sym in enumerate(line) if sym == "*"])
    return result


def find_engines(gears: list[point], data: list[str]) -> list:
    engines = []
    for item in gears:
        neighbors = get_numeric_neighbors(item, data)
        if DEBUG:
            print(f"{neighbors=}")
        if len(neighbors) == 2:
            engines.append(neighbors)

    return engines


def get_numeric_neighbors(item: point, data: list[str]) -> list:
    neighbors = []

    left = left_border = item.column - 1
    right = item.column + 1
    if left_border < 0:
        left_border = 0
    right_border = right + 1

    if DEBUG:
        print("=" * 5)

    if item.line > 0:
        new_neighbors = data[item.line - 1][left_border:right_border]
        if DEBUG:
            print(new_neighbors)
        neighbors.extend(get_numeric_in_line(item.line-1, left_border, right_border, data))


    if data[item.line][left].isnumeric():
        neighbors.append(point(item.line, left))

    if data[item.line][right].isnumeric():
        neighbors.append(point(item.line, right))

    if DEBUG:
        print(data[item.line][left], "*", data[item.line][right], sep="")

    if item.line < len(data)-1:
        new_neighbors = data[item.line + 1][left_border:right_border]
        if DEBUG:
            print(new_neighbors)
        neighbors.extend(get_numeric_in_line(item.line + 1, left_border, right_border, data))

    return [find_number_in_point(x, data) for x in neighbors]


def get_numeric_in_line(line, start, end, data) -> list[point]:
    numerics = []
    start_number = -1
    for i in range(start, end):
        if data[line][i].isnumeric():
            start_number = i
        else:
            if start_number != -1:
                numerics.append(point(line, start_number))
                start_number = -1
    if start_number != -1:
        numerics.append(point(line, start_number))
    return numerics


def find_number_in_point(p:point, data) -> int:
    s = data[p.line]
    cursor = p.column
    while cursor-1 >= 0 and s[cursor-1].isnumeric():
        cursor -= 1
    n = s[cursor]
    while cursor + 1 < len(s)-1 and s[cursor+1].isnumeric():
        n += s[cursor+1]
        cursor += 1
    return int(n)


def calculate_result(engines: list[list[int]]) -> int:
    return sum([a * b for a, b in engines])


def main():
    data = open("data.txt", "r").readlines()
    stars = find_stars(data)
    engines = find_engines(stars, data)
    result = calculate_result(engines)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
