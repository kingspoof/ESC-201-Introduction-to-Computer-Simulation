import numpy as np
import matplotlib.pyplot as plt




number_of_r_values = 100000 # number of r_values which will be estimated
last_iterations_to_plot = 100 # number of values which will be plotted for each r value
r_min, r_max = 2.8, 4 # limiting values
r_values = np.linspace(r_min, r_max, number_of_r_values)


def estimate_equilibrium(r, number_of_iterations):
    """
    Calculates the equilibrium of the current r value and returns the last 'number_of_r_values' values
    """
    x = 0.5 # the start value is not that important for this
    results = [] # we will plot the last 100 values for each r value

    for i in range(number_of_iterations):
        x = r * x * (1 - x)
        if(i >= (number_of_iterations - last_iterations_to_plot)):
            results.append(x)
    return results


output_r = []
output_x = []

for r in r_values:
    equilibrium_points = estimate_equilibrium(r, 1000)
    output_r.extend([r] * len(equilibrium_points))
    output_x.extend(equilibrium_points)



plt.figure(figsize=(10,7))
plt.plot(output_r, output_x, ',k', alpha=0.4)
plt.title("Feigenbaum Diagram")
plt.xlabel('r - value')
plt.ylabel("Equilibrium Population")
plt.xlim(r_min, r_max)
plt.ylim(0, 1)


plt.savefig('Feigenbaum_Diagramm.png', dpi=500)