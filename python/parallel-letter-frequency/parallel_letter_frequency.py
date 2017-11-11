def calculate(text_input):
    import socket
    import multiprocessing

    workers = 4
    output = {}
    dirtyText = ''
    checkText = ''

    # convert text_input into string
    for entry in text_input:
        dirtyText += entry

    # sanitize dirtyText
    for char in dirtyText:
        if char.isalpha():
            checkText += char.lower()

    def tallyLetters(checkText):
        for char in checkText:
            if char not in output:
                output[char] = 1
            else:
                output[char] += 1

    with multiprocessing.Pool(processes=workers) as pool:
        results = pool.map_async(tallyLetters(checkText), checkText)
        results.wait()


    return output
