def is_isogram(string):

    for letter in string:
        if string.lower().count(letter) > 1:
            if letter != ' ' and letter != '-':
                return False
    return True
            
        
        
