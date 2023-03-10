from string import ascii_uppercase

def set_of_letters(input):
    index = ascii_uppercase.find(input)
    return ascii_uppercase[:index + 1]

def indentNoOfSpaces(inputLetter, rowLetter):
    return ord(inputLetter) - ord(rowLetter)

def diamond_top(letter, input):
    res = ""
    space_counter = 1
    increment = 2
    for ch in input:
        if ch == "A":
            res += " " * indentNoOfSpaces(letter, ch) + ch + "\n"
        else:
            res += " " * indentNoOfSpaces(letter, ch) + ch + " " * space_counter + ch + "\n"
            space_counter = space_counter + increment

    return res[:-1]

def diamond(letter):
    letters = set_of_letters(letter)
    top = diamond_top(letter, letters)
    bot = "\n".join(list(reversed(top.split('\n')))[1:])
    return top + "\n" + bot


print(diamond("I"))