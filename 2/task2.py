from functools import reduce
from operator import mul

result = 0
data = open("data.txt", "r")
data = data.readlines()
for line in data:
    draws = (
        line[line.find(":")+2:]
        .replace("\n", "")
        .split("; ")
    )

    count = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    for draw in draws:
        pieces = draw.split(", ")
        for piece in pieces:
            piece = piece.split(" ")
            count[piece[1]] = max(count[piece[1]], int(piece[0]))

    result += reduce(mul, count.values())
    print(count, result)


print(result)