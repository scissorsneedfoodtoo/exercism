import multiprocessing
from collections import Counter

def tally_letters(text):
    tallied = Counter(text)
    return tallied

def calculate(text_input):

    checkText = ''.join(text_input).lower()
    checkText = list(filter(lambda char: char.isalpha(), checkText))

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(tally_letters, checkText)
        return sum(results, Counter())
