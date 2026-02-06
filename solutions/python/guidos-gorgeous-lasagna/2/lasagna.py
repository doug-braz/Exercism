"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time of the lasagna based on the amount of layers
    :param number_of_layers: int - indicates the amount of layers the lasagna has
    :return - returns the amount of minutes needed to preparate all the layers

    Function that calculates the amount of time needed, in minutes, to prepare a lasagna with the declared amount of layers. In this function, it is considered that each layer takes up 2 minutes to be prepared.
    
    """
    MINUTES_NEEDED_FOR_EACH_LAYER = 2
    return number_of_layers * MINUTES_NEEDED_FOR_EACH_LAYER


#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """ Calculate total time of preparation of the lasagna in minutes
    :param elapsed_time_in_minutes: int - indicates how many minutes the lasagna has been baked
    :param number_of_layers : int - indicates the number of layers the lasagna has
    :return: int - returns the amount of minutes that have been spent in the lasagna preparation

    This function takes two integers, one representing the amount of layers the lasagna in the oven has, and the other represents the amount of minutes the lasagna has stayed in the oven, and calculates the total time that has been invested so far in the lasagna preparation
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    
