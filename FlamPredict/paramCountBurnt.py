import numpy as np
from tkinter.tix import Tree
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import math
from matplotlib import animation
from matplotlib import colors


def countburnt():
    file = open("routput.txt", 'r')
    X = np.loadtxt(file)

    with open('simulateTimeVal.txt', 'r') as timeFile:
        tlines = timeFile.readlines()

        first_line = tlines[(1 - 1)]
        first_line = first_line.strip()

    simulateTime = int(first_line)

    # burnt squares count
    flatX = X.flatten()
    flatXlen = len(flatX)
    burntSq = 0
    for i in range(flatXlen):
        if (flatX[i] != 0) and (flatX[i] <= simulateTime):
            burntSq += 1

    sqMburnt = burntSq * 900
    AcreBurnt = (sqMburnt / 4047)
    return AcreBurnt




