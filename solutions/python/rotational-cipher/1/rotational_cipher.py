def rotate(text, key):
    import string

    MAX_INDEX = 26
    LOWER_ALPHA = string.ascii_lowercase
    UPPER_ALPHA = string.ascii_uppercase

    new_text = ''

    for character in text:
        if character.isalpha():
            CURRENT_INDEX = LOWER_ALPHA.index(character.lower())
            if character.islower():
                if CURRENT_INDEX + key <= 25:
                    new_text += LOWER_ALPHA[CURRENT_INDEX + key]
                else:
                    new_text += LOWER_ALPHA[CURRENT_INDEX - (MAX_INDEX - key)]
            elif character.isupper():
                if CURRENT_INDEX + key <= 25:
                    new_text += UPPER_ALPHA[CURRENT_INDEX + key]
                else:
                    new_text += UPPER_ALPHA[CURRENT_INDEX - (MAX_INDEX - key)]
        else:
            new_text += character       

    return new_text
