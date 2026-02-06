def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    aliquot_sum = 0

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    for factor in range(1,number):
        if number % factor == 0:
            aliquot_sum += factor
            print(factor)

    if number == aliquot_sum:
        return "perfect"
    elif number < aliquot_sum:
        return "abundant"
    return "deficient"
