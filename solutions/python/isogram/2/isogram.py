def is_isogram(string):
    """
    A function that returns True if a given word is an isogram, or False otherwise
    """
    text = [letter.lower() for letter in string if letter.isalpha()] # Eliminates non alphabetic characters
    return len(text) == len(set(text)) #Checks if the number of characters in the string is equal to the unique letters that appears in the text
    
    
    #for letter in string:
    #    if string.lower().count(letter) > 1:
    #        if letter != ' ' and letter != '-':
    #            return False
    #return True
            
        
        
