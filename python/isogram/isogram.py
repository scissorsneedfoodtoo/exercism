def is_isogram(string):
    test = []
    for char in string.lower():
        if char.isalpha():
            test.append(char)
    return len(set(test)) == len(test)
