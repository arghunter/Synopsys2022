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


generationBig = []



if len(generationBig) <= intmaxGenerations:
    generationBig.append(1)
    print("GENERATION: ", len(generationBig), "OUT OF", intmaxGenerations)
    import flamlineGA

else:
    print("complete")




