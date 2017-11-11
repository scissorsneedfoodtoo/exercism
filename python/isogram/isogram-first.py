import re

def is_isogram(string):
    test = re.sub(r'(\s)|(-)', '', string.lower())
    checker = 0

    for char in test:
        if test.count(char) > 1:
            checker = test.count(char)
            break

    if checker > 0:
        return False
    else:
        return True
