import numpy as np
from matplotlib import pyplot as plt



# fixed values, given in the lecture
# assumes all distances in AU (astromical units)
SEMI_MAYOR_AXIS_a = 1
EXCENTRICITY_e = 0.5
DELTA_T = 1/100

def mean_anomaly(t):
    """
    Calculates the mean anomaly at given time t

    :param t: the time
    """
    return (2*np.pi)/(SEMI_MAYOR_AXIS_a**(3/2)) * t

def keppler_equation(E, t):
    """
    Keppler's equation is M = E - e * sin(E)
    which we need to solve for E

    Which we change to f(E) = E - e * sin(E) - M,
    to solve for f(E) = 0
    """

    return E - EXCENTRICITY_e * np.sin(E) - mean_anomaly(t)

def keppler_equation_derivative(E):
    """
    Partial derivative of the keppler equation with respect to E
    """
    return 1 - EXCENTRICITY_e * np.cos(E)

def position(E):
    """
    Calculates the current position of the planet in ins orbit, using the current E value
    """
    x = SEMI_MAYOR_AXIS_a * (np.cos(E) - EXCENTRICITY_e)
    y = SEMI_MAYOR_AXIS_a * np.sqrt(1 - EXCENTRICITY_e**2) * np.sin(E)
    return [x, y]

def solve_keppler_equation(t, x0, max_iterations=1000, accuracy=10e-10):
    """
    Solves the keppler equation for the given time t, using newtons method
    max number of iterations have priority over accuracy
    """
    xn = x0

    for _ in range(max_iterations):
        current_keppler_value = keppler_equation(xn, t)
        if(abs(current_keppler_value) > accuracy):
            # calculate the next step, and change the current x value
            xn = xn - current_keppler_value / keppler_equation_derivative(xn)
        else:
            return xn # redundant return, added for error handling
    print(f"Max number of iterations met, returning value with accuracy of {abs(current_keppler_value)}")
    return xn

def main():
    current_time = 0
    number_of_steps = 1000
    positions = np.zeros((number_of_steps, 2))


    for i in range(number_of_steps):
        # sovle the keppler equation
        current_E = solve_keppler_equation(current_time, mean_anomaly(current_time))

        positions[i] = position(current_E)
        current_time += DELTA_T


    # Plot all the positions
    plt.scatter(positions[:, 0], positions[:, 1], s=2)
    plt.scatter(0,0, s=50, color='black', edgecolors='black')

    plt.title(f"Orbit Path Simulation [a = {SEMI_MAYOR_AXIS_a}, e = {EXCENTRICITY_e}]")
    plt.xlabel("X-Position [au]")
    plt.ylabel("Y-Position [au]")

    plt.gca().set_aspect('equal')
    plt.show()

main()