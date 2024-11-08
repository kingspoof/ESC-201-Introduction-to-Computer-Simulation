# imports
from numpy import sign



# Instructions
# Implement the bisection root finding algorithm presented in the first lecture for a function f
# of your choice (eg. x^x - 100 = 0 or the quadratic function f(x) = ax^2 + bx + c, for which 
# you can compare to the enalytical result)!


# definition of the function to be used
def root_f(x):
    # by geogebra, we want to find: x = 3.5972850235......
    return x**x - 100



def bisectional_root_solver(function, start_a, start_b, accuracy = 10**-10, max_iterations = 100000):
    """
    bisectional_root_solver solves for the root of any given function using the bisectional algorithm
    Will find only one root at a time. Finding multiple roots can not be guaranteed and depends on the start conditions

    :param function: The function for which the root will be found
    :param start_a: Initial x value
    :param start_b: Second initial x value, function(start_b) should have the opposite sign as function(start_a)
    :param accuracy: Value smaller than 1. Max allowed deviation from 0 to be accepted as a root
    :param max_iterations: Max number iterations before the current root is returned

    :returns: x value with function(x) < accuracy (aka the root of the function if accuracy small enough)
    """

    # check that the signs of the two functions are different and that neither of the start values are the roots themselve
    if(function(start_a) * function(start_b) > 0):
        raise ValueError('Check your input. Both start values hate the same sign')
    
    # check if the function for either points gives us the desired accuracy already
    if(function(start_a) == accuracy):
        return start_a
    elif(function(start_b) < accuracy):
        return start_b

    # assign the start variables with regards to their sign
    if(sign(function(start_a)) > 0): 
        positive_x, negative_x = start_a, start_b
    else:
        positive_x, negative_x = start_b, start_a

    current_point, current_value = 0, 0
    for _ in range(max_iterations):
        current_point = 0.5 * (positive_x + negative_x)
        current_value = function(current_point)

        # check if we have the desired accuracy already
        if(abs(current_value) < accuracy):
            return current_point
        
        # else, check with side of the bounds to override
        if(current_value > 0):
            positive_x = current_point
        else:
            negative_x = current_point

        
    # return in case the max number of iterations is exceeded
    return current_point


print(bisectional_root_solver(root_f, 0, 5))