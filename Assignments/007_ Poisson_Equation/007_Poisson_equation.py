#!/usr/bin/env python3
from scipy import ndimage
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#number of grid points
N = 100

#omega definition
w = 1.9

#define empty grid voltage
U = np.zeros((N,N))

#boundary conditions
#border of box
R = np.ones_like(U)*w/4
R[0,:] = 0
R[-1,:] = 0
R[:,0] = 0
R[:,-1] = 0

##################building components######################
center_row = int(N/2)
columns_start = int(N/4)
U[int(N/2), int(N/4):(int(N/4)+int(N/2))] = 1000
R[....] = 0

print(U)

C = np.ones_like(U)
M = np.ones_like(U)

#checker board
B = np.ones_like(U, dtype = bool)
B[....] = False
B[....] = False

#count steps
nsteps = 0

diff = np.max(np.abs(M))
#iterate until voltage change is smaller than 1e-3
while diff >= 1e-3:
    print(nsteps,diff)
    M = ....
    U = U + M ....
    nsteps += 1
    diff = np.max(np.abs(M))

plot ....



###########
W = np.array([[0,1,0],[1,-4,1],[0,1,0]])
ndimage.convolve(U,W, output = C, mode = "constant", cval = 0)
M  = ....
U[B] = U[B] + M[B]
ndimage.convolve(U,W, output = C, mode = "constant", cval = 0)
M  = ....
U[~B] = U[~B] + M[~B]


C[....] = U[....] + U[....] + U[....] + U[....] - 4.0*U[....]
M  = ....
C[....] = U[....] + U[....] + U[....] + U[....] - 4.0*U[....]
M  = ....
U[~B] = U[~B] + M[~B]
##########