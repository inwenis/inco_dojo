from string import ascii_uppercase

def set_of_letters(input):
    index = ascii_uppercase.find(input)
    return ascii_uppercase[:index + 1]

def letters(input):
    letters = set_of_letters(input)
    rev = "".join(reversed(letters))
    return letters + rev[1:]

def indentNoOfSpaces(inputLetter, rowLetter):
    return ord(inputLetter) - ord(rowLetter)

def add_new_lines(input):
    res = ""
    space_counter = 1
    increment = 2
    middle = len(input)//2
    for (idx,ch) in enumerate(input):
        if ch == "A":
            res += " " * indentNoOfSpaces(input[middle], ch) + ch + "\n"
        else:
            res += " " * indentNoOfSpaces(input[middle], ch) + ch + " " * space_counter + ch + "\n"
            if idx == middle:
                increment = -2
            space_counter = space_counter + increment

    return res[:-1]

def diamond(input):
    return letters(input)


print(add_new_lines(letters("C")))