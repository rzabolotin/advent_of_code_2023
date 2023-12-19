limitations = {
    "red": 12,
    "green": 13,
    "blue": 14
}

result = 0
data = open("data.txt", "r")
data = data.readlines()
for line in data:
    game_number = line[5:line.find(":")]
    draws = (
        line[line.find(":")+2:]
        .replace("\n", "")
        .split("; ")
    )
    game_is_bad = False
    for draw in draws:
        pieces = draw.split(", ")
        for piece in pieces:
            piece = piece.split(" ")
            if limitations[piece[1]] < int(piece[0]):
                game_is_bad = True

    if not game_is_bad:
        result += int(game_number)
        print(result, game_number)

print(result)