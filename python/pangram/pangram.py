import re

def is_pangram(sentence):
    check = re.sub('[^a-z]+', '', sentence.lower())

    return len(set(check)) == 26
