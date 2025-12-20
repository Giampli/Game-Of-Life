def parse_coordinates(path):
    coords = []
    with open(path, "r") as f:
        y = 0
        for line in f:
            if line.startswith("!"):
                continue
            line = line.rstrip("\n")
            for x, ch in enumerate(line):
                if ch == "O":
                    coords.append([x, y])
            y += 1
    return coords

# example usage:
result = parse_coordinates("gosperguninlineinverter.cells")
print(result)
