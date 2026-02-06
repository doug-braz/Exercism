def is_armstrong_number(number):
    """
    is_armstrong_number is a function designed to point if a given number is an armstrong number or
    not
    @param number (int): is the number to check if it fits the Armstrong number description or not
    @return value - Bool: True if number is an Armstrong number, false if it is not
    """
    str_number = str(number)
    sum = 0
    for digit in str_number:
        sum += int(digit)**len(str_number)
    if sum == number:
        return True
    return False
        
