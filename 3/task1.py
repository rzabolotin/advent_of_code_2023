from collections import namedtuple

gear = namedtuple("gear", "line start end number")
DEBUG = False


def parse_data(data: list[str]) -> list[gear]:
    gears_info = []
    for (line_no, line) in enumerate(data):
        current_start = -1
        column = 0
        for (column, symbol) in enumerate(line):
            if symbol.isnumeric():
                if current_start == -1:
                    current_start = column
            else:
                if current_start != -1:
                    gears_info.append(gear(line_no, current_start, column - 1, line[current_start:column]))
                current_start = -1
        if current_start != -1:
            print(current_start)
            gears_info.append(gear(line_no, current_start, column, line[current_start:column]))
    return gears_info


def filter_gears_with_neighboors(gears: list[gear], data: list[str]) -> list[gear]:
    correct_gears = []
    for gear in gears:
        if get_neighboors(gear, data):
            correct_gears.append(gear)

    return correct_gears


def get_neighboors(gear: gear, data: list[str]) -> list[str]:
    neighbors = []

    left = left_border = gear.start -1

    if left_border < 0:
        left_border = 0
    right = gear.end + 1
    right_border = right + 1

    if DEBUG:
        print("=" * 5)

    if gear.line > 0:
        new_neighbors = data[gear.line - 1][left_border:right_border]
        neighbors.extend(new_neighbors)
        if DEBUG:
            print(new_neighbors)

    neighbors.append(data[gear.line][left])
    neighbors.append(data[gear.line][right])
    if DEBUG:
        print(data[gear.line][left], gear.number, data[gear.line][right], sep="")

    if gear.line < len(data)-1:
        new_neighbors = data[gear.line + 1][left_border:right_border]
        neighbors.extend(new_neighbors)
        if DEBUG:
            print(new_neighbors)

    return [x for x in neighbors if x != "." and x != "\n"]


def main():
    data = open("data.txt", "r").readlines()
    gears_info = parse_data(data)
    correct_gears = filter_gears_with_neighboors(gears_info, data)
    result = sum(int(g.number) for g in correct_gears)
    print(f"Result sum: {result}")


if __name__ == "__main__":
    main()
