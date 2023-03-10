from string import ascii_uppercase

def set_of_letters(input):
    index = ascii_uppercase.find(input)
    return ascii_uppercase[:index + 1]

def indentNoOfSpaces(inputLetter, rowLetter):
    return ord(inputLetter) - ord(rowLetter)

def diamond_top(letter, input):
    res = []
    space_counter = 1
    increment = 2
    for ch in input:
        if ch == "A":
            res.append(" " * indentNoOfSpaces(letter, ch) + ch)
        else:
            res.append(" " * indentNoOfSpaces(letter, ch) + ch + " " * space_counter + ch)
            space_counter = space_counter + increment

    return res

def diamond(letter):
    letters = set_of_letters(letter)
    top = diamond_top(letter, letters)
    bot = list(reversed(top))[1:]
    return "\n".join(top + bot)


print(diamond("I"))