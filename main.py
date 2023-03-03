def add(input):
    if input.startswith("//"):
        input = input[4::]

    if not input:
        return 0

    token = input.replace("\n", ",").split(",")
    return sum([int(x) for x in token])