def is_paired(input_string):
    OPENING_SYMBOLS = ('(','{','[')
    CLOSING_SYMBOLS = (')','}',']')

    MATCHING_SYMBOLS = {
        ')':'(',
        ']':'[',
        '}':'{'
    }

    open = []
    close = []

    for character in input_string:
        if character in OPENING_SYMBOLS:
            open.append(character)
        elif character in CLOSING_SYMBOLS:
            if open:
                if MATCHING_SYMBOLS[character] != open[-1]:
                    return False
                else:
                    open.pop(-1)
            else:
                return False
    if not open:
        return True
    else:
        return False
