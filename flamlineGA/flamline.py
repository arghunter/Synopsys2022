import time
from tkinter.tix import Tree
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import animation
from matplotlib import colors
from queue import Queue
import threading
import random


# import files and variables

from userInfo import *
from genome import *
gnme = Genome(10)
gnmeQ = gnme.bx.qsize()
# for i in range(gnmeQ):
     # print(str("("+str(gnme.v[i][1]))+","+str(gnme.v[i][0])+")")
     # print(str("(" + str(gnme.bx.get())) + "," + str(gnme.by.get()) + ")")

########################################################################

# scaling: each box is 20m (0.02km) by 20m (0.02km)
# fire spreads at 1kmh
# each minute is an hour
# 50 ticks an minute (1kmh)
# 1.2s per tick
# each tick is 1 minute and 12 seconds of spread in real life.

########################################################################

# The neightbors of a cells
neighborhood = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                (0, 1), (1, -1), (1, 0), (1, 1))
# Cell types for automata
EMPTY, TREE, FIRE, BURNT, LINE = 0, 1, 2, 3, 4
# Color corresponds to cell type
colors_list = [(0.2, 0, 0), (0, 0.5, 0), (1, 0, 0),
               (1, 0.65, 0), (1, 1, 1), (0, 0, 0)]
cmap = colors.ListedColormap(colors_list)

# The bounds list must also be one larger than the number of different values in
# the grid array.
bounds = [0, 1, 2, 3, 4, 5, 6]

# Maps the colors in colors_list to bins defined by bounds; data within a bin
# is mapped to the color with the same index.
norm = colors.BoundaryNorm(bounds, cmap.N)


# lists location
tickElapsed = []
currentBurntList = []
totalBurntList = []
threadDone = 0


def loopFire(X, FIRESX, FIRESY, A):
    while True:
        firerules(X, FIRESX, FIRESY, A)


def popForest(X):
    # X1 is the future state of the forest; ny and nx (defined as 100 later in the
    # code) represeent the number of cells in the x and y directions, so X1 is an
    # array of 0s with 100 rows and 100 columns).
    # RULE 1 OF THE MODEL is handled by setting X1 to 0 initially and having no
    # rules that update FIRE cells.
    X1 = np.zeros((ny, nx))
    # For all indices on the grid excluding the border region (which is always empty).
    # Note that Python is 0-indexed.
    for ix in range(1, nx - 1):
        for iy in range(1, ny - 1):
            # THIS CORRESPONDS TO RULE 4 OF THE MODEL. If the current value at
            # the index is 0 (EMPTY), roll the dice (np.random.random()); if the
            # output float value <= p (the probability of a tree being growing),
            # the future value at the index becomes 1 (i.e., the cell transitions
            # from EMPTY to TREE).
            if X[iy, ix] == LINE:
                X1[iy, ix] = LINE
            # if X[iy, ix] == EMPTY and np.random.random() <= p:
            #     X1[iy, ix] = TREE
            # THIS CORRESPONDS TO RULE 2 OF THE MODEL.
            # If any of the 8 neighbors of a cell are burning (FIRE), the cell
            # (currently TREE) becomes FIRE based on a spread chance.
            if X[iy, ix] == TREE:
                X1[iy, ix] = TREE
                for iyf in range(iy - 20, iy + 20):
                    for ixf in range(ix - 20, ix + 20):
                        if (iyf > 0 and ixf > 0 and ixf < nx and iyf < ny and ((iy - iyf) ** 2 + (
                                ix - ixf) ** 2 < 400 or np.random.random() <= f * 100) and np.random.random() < p):
                            X1[iyf, ixf] = TREE
                # To examine neighbors for fire, assign dx and dy to the
                # indices that make up the coordinates in neighborhood. E.g., for
                # the 2nd coordinate in neighborhood (-1, 0), dx is -1 and dy is 0.

                for dx, dy in neighborhood:
                    if X[iy + dy, ix + dx] == FIRE and np.random.random() <= spread_chance:
                        X1[iy, ix] = FIRE
                        break
                # THIS CORRESPONDS TO RULE 3 OF THE MODEL.
                # If no neighbors are burning, roll the dice (np.random.random());
                # if the output float is <= f (the probability of a lightning
                # strike), the cell becomes FIRE.
                # else:
                #	if np.random.random() <= f:
                # 	X1[iy,ix] = FIRE
                # initial fire

    return X1


def popAltSeg(A, ix, iy):
    A[iy][ix] = 1

    # if(np.random.random() < 0.3):
    #     A[iy][ix] = -1

    # print("Altitude"+str(ix)+" "+str(iy))
    # print("("+str(ix)+","+str(iy)+")")

    A[iy][ix] = A[iy][ix]*240*np.random.random()+80*A[iy][ix]
    # d = np.random.random()*200

    for tx in range(ix-80, ix+80):
        # print(tx-ix)
        for ty in range(iy-80, iy + 80):

            if((tx-ix)**2 + (ty-iy)**2 <= (80)**2 and A[ty][tx] != 1):

                if(A[iy][ix] < 0):
                    t = A[iy][ix] + \
                        (abs(tx-ix) + abs(ty-tx))/2
                    A[ty][tx] -= abs(t)
                else:
                    t = A[iy][ix] - \
                        (abs(tx-ix) + abs(ty-tx))/2
                    A[ty][tx] += abs(t)

                    # if(t >= 0):
                    #     A[ty][tx] += t

                if A[ty][tx] == 1:
                    A[ty][tx] = 2
                    # print("("+str(ty)+","+str(tx)+")")
                    # print(str(iy)+" "+str(ix) + " " + str(ty) +
                    #       " "+str(tx)+" "+str(A[ty][tx]))
    A[1023][1023] = A[1023][1023]-1


def popAltitude(A):

    tc = 0
    for i in range(0, 1024):
        tc += 1
        tx = int(random.random() * (nx - 160)) + 80
        ty = int(random.random() * (ny - 160)) + 80
        t = (threading.Thread(target=popAltSeg, args=(
            A, tx, ty)))
        statusAltPop = float(((int(tc)) / 1024))
        percentAltPop = math.ceil((statusAltPop * 100))
        print("Altitude Generated: ", tc, "Out Of", "1024", "----------", int(percentAltPop), "%")
        t.start()

    # for ix in range(1, nx - 1):
    #     # print(A[ix])

    while A[1023][1023] != -1024:
        time.sleep(1)
        print(
            A[1023][1023])

    # for ix in range(1, nx - 1):
    #     print(A[ix])


def firerules(X, FIRESX, FIRESY, A):
    # print(len(FIRES))
    qs = FIRESX.qsize()
    centery = int((ny / 2))
    centerx = int((nx / 2))
    print("tick #:", str(int(len(tickElapsed))))
    # sideLength = 100

    if int(len(tickElapsed)) >= iUD:
        queueSizeLine = int(gnme.bx.qsize())
        if queueSizeLine >= lineDrawSpeed:
            for i in range(lineDrawSpeed):
                X[gnme.by.get()][gnme.bx.get()] = LINE
        elif queueSizeLine != 0 and queueSizeLine <= lineDrawSpeed:
            for i in range(int(queueSizeLine)):
                X[gnme.by.get()][gnme.bx.get()] = LINE
        else:
            print("Line Draw Finished")

    # if(qs == 0):
    #     xt = int(int(np.random.random()*len(tickElapsed))-len(tickElapsed)/2)
    #     yt = int(int(np.random.random()*len(tickElapsed))-len(tickElapsed)/2)
    #     X[yt][xt] = FIRE
    #     FIRESX.put(xt)
    #     FIRESY.put(yt)

    while (qs > 0):
        qs -= 1
        x1 = int(FIRESX.get())
        y1 = int(FIRESY.get())
        X[y1][x1] = EMPTY

        for dx, dy in neighborhood:

            if int(y1) + dy >= 0 and int(y1) + dy < ny and int(x1) + dx >= 0 and int(x1) + dx < nx and X[
                    int(y1) + dy, int(x1) + dx] == TREE and np.random.random() <= spread_chance+(A[y1+dy][x1+dx]-A[y1][x1])/(1200.0):
                # print(spread_chance+(A[y1+dy][x1+dx]-A[y1][x1])/(2000))
                X[int(y1) + dy, int(x1) + dx] = FIRE
                FIRESX.put(int(x1) + dx)
                FIRESY.put(int(y1) + dy)

    return X


# Forest size (number of cells in x and y directions).
# nx, ny = 1024, 1024
# Initialize the forest grid. X can be thought of as the current state. Make X an
# array of 0s.
FIRESX = Queue(maxsize=0)
FIRESY = Queue(maxsize=0)
FIRESY.put(int(ny / 2))
FIRESX.put(int(nx / 2))
# FIRES[0, 0] = int(ny/2)
# FIRES[0, 1] = int(nx/2)

X = np.zeros((ny, nx))
A = np.zeros((ny, nx))  # the altitude of the ground


# X[1:ny-1, 1:nx-1] grabs the subset of X from indices 1-99 EXCLUDING 99. Since 0 is
# the index, this excludes 2 rows and 2 columns (the border).
# np.random.randint(0, 2, size=(ny-2, nx-2)) randomly assigns all non-border cells
# 0 or 1 (2, the upper limit, is excluded). Since the border (2 rows and 2 columns)
# is excluded, size=(ny-2, nx-2).
X[1: (ny - 1), 1: (nx - 1)] = np.random.randint(0, 2, size=(ny - 2, nx - 2))

# This ensures that the number of 1s in the array is below the threshold established
# by forest_fraction. Note that random.random normally returns floats between
# 0 and 1, but this was initialized with integers in the previous line of code.
X[1: (ny - 1), 1: (nx -
  1)] = np.random.random(size=(ny - 2, nx - 2)) < forest_fraction / 300 + 0.00001
X[int(ny / 2) + 1][int(nx / 2) + 1] = TREE
X[int(ny / 2) - 1][int(nx / 2) - 1] = TREE
X[int(ny / 2) - 1][int(nx / 2) + 1] = TREE
X[int(ny / 2)][int(nx / 2)] = FIRE
# X[int(ny/2)+1][int(nx/2)-1] = TREE
X = popForest(X)
# line bounds
# define A values
popAltitude(A)

# list ranges after A values are defined
xAltList = list(range(0, int(nx)))
yAltList = list(range(0, int(ny)))

t1 = threading.Thread(target=loopFire, args=(X, FIRESX, FIRESY, A))
# Adjusts the size of the figure.

fig = plt.figure(figsize=(25 / 3, 6.25))


# Creates 1x1 grid subplot.
ax = fig.add_subplot(111)


# Turns off the x and y axis.
# ax.set_axis_off()


# The matplotlib function imshow() creates an image from a 2D numpy array with 1
# square for each array element. X is the data of the image; cmap is a colormap;
# norm maps the data to colormap colors.
im = ax.imshow(X, cmap=cmap, norm=norm)  # , interpolation='nearest')


# The animate function is called to produce a frame for each generation.


# for things that are done every tick, do them here:
def animate(i):
    # animate figure
    im.set_data(animate.X)
    animate.X = firerules(animate.X, animate.FIRESX, animate.FIRESY, animate.A)

    # track number of ticks elapsed
    tickElapsed.append(1)

    # track current burnt squares using queue size
    currentBurnt = FIRESX.qsize()
    currentBurntList.append(currentBurnt)

    if int(len(tickElapsed)) >= iUD:
        if int(currentBurnt) == 0:
            print("fire over")
            fireStatus = False
            anim.event_source.stop()
            print("dbg: anim stopped")
            quit()


    # sum currentBurnt for total squares burnt
    totalBurnt = sum(currentBurntList)
    # append to list for future record
    totalBurntList.append(totalBurnt)
    # print current total burnt = current score
    print("totalBurnt: ", totalBurnt)


# Binds the grid to the identifier X in the animate function's namespace.
animate.X = X
animate.A = A
animate.FIRESX = FIRESX
animate.FIRESY = FIRESY

# Interval between frames (ms).
interval = iTR

# animation.FuncAnimation makes an animation by repeatedly calling a function func;
# fig is the figure object used to resize, etc.; animate is the callable function
# called at each frame; interval is the delay between frames (in ms).
anim = animation.FuncAnimation(fig, animate, interval=interval)


# figure 2 for contour
# plt.figure(2)
# draw contour

# only figure 1 for now
plt.figure(1)
# figure 2 for contour
# plt.figure(2)
# draw contour

plt.contour(xAltList, yAltList, A)
plt.colorbar()


# Display the animated figure
plt.show()
