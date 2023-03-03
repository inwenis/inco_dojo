def sanitize_input(input):
    if input.startswith("//"):
        custom_deli = input[2]
        return input[4::].replace(custom_deli, ",")
    return input
def add(input):
    input = sanitize_input(input)

    if "-" in input:
        raise Exception(f"negatives not allowed: {input}")

    token = []
    if input:
        token = input.replace("\n", ",").split(",")
    return sum([int(x) for x in token])