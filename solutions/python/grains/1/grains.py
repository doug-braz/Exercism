def square(number):
    """
    Evaluates the number of grains that is cointained in a given square of the chess board
    Param. number: indicates the number of the square in which the number of grains is desired to know
    Return value: number of grains contained in the desired square
    """

    if (1<= number <= 64):
        return 2**(number-1)
    else:
        raise ValueError('square must be between 1 and 64')
    
  


def total():
    """
    Calculates the total number of grains contained in the chess board
    Return value: number of grains contained in the entire chessboard
    """
    total_number_of_grains = 0
    for i in range(1, 65):
        total_number_of_grains += 2**(i-1)
    return total_number_of_grains
