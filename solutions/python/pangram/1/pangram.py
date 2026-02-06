def is_pangram(sentence):
    """
    Funcion is_pangram is developed to inform if a given sentence is or isn't a pangram, that is
    a sentence that cointains all the 26 letters of the alphabet
    param. sentence - string: informs the sentence to be determined if it is a pangram
    return value: boolean: returns True if the given is a pangram, and False if it isn't
    """
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
               'n','o','p','q','r','s','t','u','v','w','x','y','z']
    counter = 0
    for letter in sentence:
        if letter.lower() in alphabet:
            counter += 1
            alphabet.remove(letter.lower())
    if counter == 26:
        return True
    return False
        
