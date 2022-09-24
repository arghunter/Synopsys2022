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


# altitude init
# from altitudeGen import *

# genome init
from genome import *


# create Genome objects and sizes
gnme_var_holder = {}
gnme_Q_var_holder = {}

for x in range(0, intmaxPopSize):
    gnme_var_holder['gnme' + str(x)] = Genome(vertexNum)

globals().update(gnme_var_holder)

for x in range(0, intmaxPopSize):
    gnme_Q_var_holder['gnmeQ' + str(x)] = (globals()['gnme' + str(x)]).bx.qsize()

globals().update(gnme_Q_var_holder)

print("gnme 0", gnme0)
print("size gnme0", gnmeQ0)

print("gnme 0", gnme1)
print("size gnme0", gnmeQ1)

# scores
score_var_holder = {}

for x in range(0, intmaxPopSize):
    score_var_holder['score' + str(x)] = 0

globals().update(score_var_holder)

############################################################

# other init



############################################################

# lists for gen status

genComplete = []
popComplete = []



# fire status
fireStatus = 1

# Generation Run
for i in range(int(intmaxGenerations - 1)):
    genComplete.append(1)

    print("GENERATION: ", len(genComplete), "OUT OF", intmaxGenerations)

    for i in range(int(intmaxPopSize - 1)):
        popComplete.append(1)

        print("INDIVIDUAL: ", len(popComplete), "OUT OF", intmaxPopSize)
        exec(open('flamline.py').read())
        print("score", len(popComplete), ":", (globals()['score' + str((len(popComplete) - 1))]))














    # population in generation
    # if len(populationBig) <= intpopulationSize:
    #     populationBig.append(1)
    #     print("POPULATION: ", len(populationBig), "OUT OF", intpopulationSize)


