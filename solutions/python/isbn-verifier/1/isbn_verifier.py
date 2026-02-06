def is_valid(isbn):
    import string
    alphabet = list(string.ascii_lowercase)
    for char in isbn:
        if char.lower() in alphabet and char.lower() != 'x':
            return False
    clean = [character for character in isbn if (character.isnumeric() or character.lower() == 'x')]
    verifying_sum = 0
    counter = 1

    if len(clean) != 10:
        return False
    for char in clean:

        if char.lower() != 'x':
            verifying_sum += int(char)*(10 - counter + 1)
        else:
            verifying_sum += 10
        counter += 1
                    
    return verifying_sum % 11 == 0
        
        
    
