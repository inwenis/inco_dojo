from string import ascii_uppercase

def set_of_letters(input):
    index = ascii_uppercase.find(input)
    return ascii_uppercase[:index + 1]

def indentNoOfSpaces(inputLetter, rowLetter):
    return ord(inputLetter) - ord(rowLetter)

def add_new_lines(input):
    res = ""
    space_counter = 1
    increment = 2
    middle = len(input) - 1
    for ch in input:
        if ch == "A":
            res += " " * indentNoOfSpaces(input[middle], ch) + ch + "\n"
        else:
            res += " " * indentNoOfSpaces(input[middle], ch) + ch + " " * space_counter + ch + "\n"
            space_counter = space_counter + increment

    return res[:-1]

def diamond(input):
    return set_of_letters(input)

def diamond(letter):
    l = set_of_letters(letter)
    top = add_new_lines(l)
    bot = "\n".join(list(reversed(top.split('\n')))[1:])
    return top + "\n" + bot


print(diamond("I"))