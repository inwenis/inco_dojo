def add(input):
    if input.startswith("//"):
        custom_deli = input[2]
        input = input[4::].replace(custom_deli, ",")

    token = []
    if "-" in input:
        raise Exception(f"negatives not allowed: {input}")
    
    if input:
        token = input.replace("\n", ",").split(",")
    return sum([int(x) for x in token])