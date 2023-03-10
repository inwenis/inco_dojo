from string import ascii_uppercase

def set_of_letters(input):
    index = ascii_uppercase.find(input)
    return ascii_uppercase[:index + 1]

def letters(input):
    letters = set_of_letters(input)
    rev = "".join(reversed(letters))
    return letters + rev[1:]

def add_new_lines(input):
    res = ""
    for ch in input:
        if ch == 'A':
            res += ch + "\n"
        else:
            res += ch + ch + "\n"
    return res[:-1]

def diamond(input):
    return letters(input)


