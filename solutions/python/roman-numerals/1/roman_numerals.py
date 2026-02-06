def roman(number):
    roman_representation = ''
    if number/1000 >= 1:
        roman_representation += number//1000 * 'M'
    number -= (number//1000)*1000
    if number//100 == 9:
        roman_representation += 'CM'
    if 5 <= number//100 < 9 :
        roman_representation += 'D' + (number//100 - 5) * 'C'
    if number//100 == 4:
        roman_representation += 'CD'
    if 1 <= number//100 < 4:
        roman_representation += number//100 * 'C'
    number -= (number//100)*100
    if number//10 == 9:
        roman_representation += 'XC'
    if 5 <= number//10 <= 8:
        roman_representation += 'L' + (number//10 - 5)*'X'
    if number//10 == 4:
        roman_representation += 'XL'
    if 1 <= number//10 <= 3:
        roman_representation += number//10 * 'X'
    number -= (number//10)*10
    if number == 9:
        roman_representation += 'IX'
    if 5 <= number <= 8:
        roman_representation += 'V' + (number-5) * 'I'
    if number == 4:
        roman_representation += 'IV'
    if 1 <= number <= 3:
        roman_representation += number * "I"
        

    return roman_representation

