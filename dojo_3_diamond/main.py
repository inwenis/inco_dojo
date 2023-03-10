from string import ascii_uppercase

def set_of_letters(input):
    index = ascii_uppercase.find(input)
    return ascii_uppercase[:index + 1]

def letters(input):
    letters = set_of_letters(input)
    rev = "".join(reversed(letters))
    return letters + rev[1:]

def diamond(input):
    return letters(input)


