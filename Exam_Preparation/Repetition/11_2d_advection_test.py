import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def normal_distribution(x, y, A=1, sx=5, sy=5, x0=25, y0=25):
    return A * np.exp(-((x-x0)**2/(2*sx**2) + (y - y0)**2/(2*sy**2)))


def cir_method(grid, ca=0.2, cb=0.5):
    new_grid = grid - ca * (grid - np.roll(grid, 1, axis=0)) - cb * (grid - np.roll(grid, 1, axis=1))
    return new_grid



size = 100
Z = np.ones((size, size))

for x in range(size):
    for y in range(size):
        Z[x, y] = normal_distribution(x, y)


iterations = 100
grids = [Z]
for i in range(iterations):
    grids.append(cir_method(grids[-1]))


fig, ax = plt.subplots()
img = ax.imshow(grids[0], cmap='viridis', origin='lower')

def update(frame):
    img.set_array(grids[frame % len(grids)])
    return img

anim = animation.FuncAnimation(fig, update, frames=len(grids))
writer = animation.PillowWriter(fps=30)
anim.save(f"animation.gif", writer=writer)