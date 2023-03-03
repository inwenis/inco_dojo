def add(input):
    if "," in input:
        token = input.split(",")
        return int(token[0]) + int(token[1])

    if input:
        return int(input)

    return 0
