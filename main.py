def add(input):
    if not input:
        return 0

    token = input.split(",")
    return sum([int(x) for x in token])