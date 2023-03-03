def add(input):
    if not input:
        return 0

    if "\n" in input:
        token = input.split("\n")
        return sum([int(x) for x in token])

    token = input.split(",")
    return sum([int(x) for x in token])