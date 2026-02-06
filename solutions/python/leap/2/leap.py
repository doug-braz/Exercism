def leap_year(year):
    """
    leap_year is a function designed to indicate if a given year is a leap year or not in the
    Gregorian Calendar
    @param year(int): indicates the year that is desired to know if it is a leap year or not
    @return value(bool): True if it is a leap year, false if it isn't
    """
    
    return year % 4 == 0 and year % 100 !=0 or (year % 100 == 0 and year % 400 == 0)
