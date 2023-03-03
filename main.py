def add(input):
    if not input:
        return 0

    if "\n" in input:
        return int(input[0]) + int(input[2])

    token = input.split(",")
    return sum([int(x) for x in token])