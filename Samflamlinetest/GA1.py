import time
from tkinter.tix import Tree
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import animation
from matplotlib import colors
from queue import Queue
import threading

# import files
from userInfo import *

maxGenerations = input("Number of Generations: ")
intmaxGenerations = int(maxGenerations)

populationSize = input("Population Size in Each Generation: ")
intpopulationSize = int(populationSize)

iFSS = iFSS
iTR = iTR
iLDSS = iLDSS
iLDSST = iLDSST
iUD = iUD
iBS = iBS
iTau = iTau
upTau = upTau
sideLength = sideLength


generationBig = []
populationBig = []

fireStatus = True

if len(generationBig) <= intmaxGenerations:
    generationBig.append(1)
    print("GENERATION: ", len(generationBig), "OUT OF", intmaxGenerations)

    
    from flamlineGA import *



else:
    print("complete")




