import numpy as np
import matplotlib.pyplot as plt



def bounds(val, values, order=1):
    """
    Returns the values of the list, where the lower value is the next 
    lower value from the list and the opper is the next higher value in the grid

    eg:
        list = [0, 1, 2, 3, 4, 5, 6]
        value = 2.5
    returns:
        2, 3
    """

    lower = [x for x in values if x <= val]
    higher = [x for x in values if x >= val]

    return max(lower), min(higher)

def bilinear_interpolation(point, x_values, y_values, z_values):
    """
    Estimates the value of the points in the 3d space from the given values

    parameters:
        points (float, float): value at which z will be estimated
        x_values (numpy float array): x_values of the system
        y_values (numpy float array): y_values of the system
        z_grid (numpy 2d float array): a NxN array with the height values
    returns:
        float: z height of the point
    """

    # validate that the points lies inbetween 4 of our points
    x, y = point

    x_lower, x_upper = bounds(x, x_values)
    x_lower_index, x_upper_index = np.where(x_values == x_lower)[0], np.where(x_values == x_upper)[0]
    y_lower, y_upper = bounds(y, y_values)
    y_lower_index, y_upper_index = np.where(y_values == y_lower)[0], np.where(y_values == y_upper)[0]

    t = x - x_lower
    u = y - y_lower

    f1 = z_values[x_lower_index, y_lower_index]
    f2 = z_values[x_upper_index, y_lower_index]
    f3 = z_values[x_lower_index, y_upper_index]
    f4 = z_values[x_upper_index, y_upper_index]

    f = (1 - t) * (1 - u) * f1 + t * (1 - u) * f2 + u * (1-t)*f3 + u * t * f4
    
    return f


""" Define data """
size = 3
x = np.linspace(0, 1, size)
y = np.linspace(0, 1, size)
z = np.random.rand(size, size)

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111, projection='3d')

# plot the given values
X, Y = np.meshgrid(x, y)
Z = z
ax.scatter(X.ravel(), Y.ravel(), Z.ravel(), c='b')  # Flatten arrays

# plot the calculated values
x_space = np.linspace(0, 1, 5)
y_space = np.linspace(0, 1, 5)
X1, Y1 = np.meshgrid(x_space, y_space)
z_self = np.random.rand(5, 5)


for i, xi in enumerate(x_space):
    for j, yj in enumerate(y_space):
        z_self[i, j] = bilinear_interpolation((xi, yj), x, y, z)


ax.scatter(X1.ravel(), Y1.ravel(), z_self.ravel(), c='r', s=5)
ax.plot_surface(X, Y, Z)

plt.show()








plt.show()