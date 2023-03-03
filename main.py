def add(input):
    if not input:
        return 0

    if "\n" in input:
        token = input.split("\n")
        return int(token[0]) + int(token[1])

    token = input.split(",")
    return sum([int(x) for x in token])