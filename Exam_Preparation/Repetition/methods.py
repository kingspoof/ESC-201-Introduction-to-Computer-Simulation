import numpy as np





""" Bisection Root Finding algorithm """
def bisection_root_finding(f):
    """ Define some functional constants """
    max_starting_values = 10e10
    starting_value_increase = 10
    accuracy_threshhold = 10e-20     # limit the run time of the function by defining a required accuracy
    max_iterations = 10000           # limit the run time of the function -> disregards accuracy

    # first we try and find two different points with a differnt sign
    starting_value = 1
    while(np.sign(f(starting_value)) * np.sign(f(-1 * starting_value)) == 1):
        starting_value += starting_value_increase
    #print(f"Found Starting conditions: {-starting_value} -> {starting_value}")


    # assign the values according to their sign
    positive_x = starting_value if np.sign(starting_value) > 0 else -1 * starting_value
    negative_x = -starting_value
    #print(f"Positive X: {positive_x}, Negative_x: {negative_x}")


    # now that we have our starting conditions, we can find the root
    current_iteration = 0
    current_x_value = 0.5 * (positive_x + negative_x)
    current_function_value = f(current_x_value)
    while(np.abs(current_function_value) > accuracy_threshhold and current_iteration < max_iterations):
        if(current_function_value > 0):
            positive_x = current_x_value
        else:
            negative_x = current_x_value

        current_x_value = 0.5 * (positive_x + negative_x)
        current_function_value = f(current_x_value)


        current_iteration += 1


    return current_x_value


""" Newtons Root finding algorithm """
def newton_root_finding(f, x0 = 0):
    accuracy_threshhold = 1e-5
    max_iterations = 10e5
    
    # we use this to compute the derivative
    def df(x):
        h = 1e-5
        return (f(x+h) - f(x))/(h)


    current_iteration = 0
    current_x_value = x0
    current_function_value = f(x0)
    current_derivative_value = df(x0)
    while(current_iteration < max_iterations and abs(current_function_value) > accuracy_threshhold):
        current_x_value = current_x_value - current_function_value / current_derivative_value

        current_function_value = f(current_x_value)
        current_derivative_value = df(current_x_value)

    return current_x_value