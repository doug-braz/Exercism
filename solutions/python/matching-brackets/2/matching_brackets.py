def is_paired(input_string):

    MATCHING_SYMBOLS = {
        ')':'(',
        ']':'[',
        '}':'{'
    }

    open = []

    for character in input_string:
        if character in '({[':
            open.append(character)
        elif character in ')}]':
            if not open or MATCHING_SYMBOLS[character] != open[-1]:
                return False
            else:
                open.pop(-1)

    if not open:
        return True
    return False
