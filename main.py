def add(input):
    if "," in input:
        token = input.split(",")
        return sum([int(x) for x in token])

    if input:
        return int(input)

    return 0
