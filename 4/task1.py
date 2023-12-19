from collections import namedtuple


game = namedtuple("game", "winning inhands")
DEBUG = False


def parse_data(data:list[str]) -> list[game]:
    result = []
    for line in data:
        line = line.split(":")[1]
        line = line.replace("  ", " ")
        winning, inhand = line.split("|")
        new_game = game(winning.strip().split(" "), inhand.strip().split(" "))
        result.append(new_game)
    return result


def count_points(g:game):
    count = len(set(g.winning).intersection(g.inhands))
    points = 0
    if count != 0:
        points = 2 ** (count - 1)
    if DEBUG:
        print(g)
        print(set(g.winning).intersection(g.inhands))
        print(count, points)

    return points


def main():
    data = open("data.txt", "r").readlines()
    cards = parse_data(data)
    print ({i:count_points(g) for i,g in enumerate(cards)})


if __name__ == "__main__":
    main()
