from collections import namedtuple

DEBUG = True


def parse_data(data:list[str]) -> dict[int:dict]:
    result = {}
    for i, line in enumerate(data):
        line = line.split(":")[1]
        line = line.replace("  ", " ")
        winning, inhand = line.split("|")
        intersection = len(set(winning.strip().split(" ")).intersection(inhand.strip().split(" ")))
        result[i] = dict(intersection=intersection, card_count=1)
    return result


def play_game(games: dict[int:dict]):
    for i in games:
        if DEBUG:
            print(i)
            for d in range(5):
                if (i+d) in games:
                    print(games[i + d])
            print()
        for j in range(games[i]["intersection"]):
            if (i + j + 1) in games:
                games[i + j + 1]["card_count"] += games[i]["card_count"]


def main():
    data = open("data.txt", "r").readlines()
    game = parse_data(data)
    play_game(game)
    print(sum(x["card_count"] for x in game.values()))


if __name__ == "__main__":
    main()
