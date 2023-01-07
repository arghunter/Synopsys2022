import subprocess
import numpy as np
from tkinter.tix import Tree
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import math
from matplotlib import animation
from matplotlib import colors
from paramCountBurnt import countburnt


print("Initializing")


# scorer time list
# scoreTimeList = ["790", "993", "1345", "1509", "1653", "2281"]
scoreTimeList = ["790"]
simBurnList = []


# list average
def Average(lst):
    return sum(lst) / len(lst)

# scorer
def run_scorer():
    for i in range(5):
        # run flamline
        exec(open("flamline.py").read())
        # run scorer
        SmallcbVal = countburnt()
        simBurnList.append(SmallcbVal)
    cbVal = Average(simBurnList)
    simBurnList.clear()
    return cbVal


# comparer
def comparer():
    # get actual burnt value
    with open('actualBurntVal.txt', 'r') as actFile:
        actlines = actFile.readlines()
        tActVal = actlines[(((3 * i) + 5) - 1)]
        tActVal = tActVal.strip()
    ActualBurntVal = float(tActVal)

    # get simulated burnt value
    SimBurntVal = run_scorer()

    # find percent error from simulated burnt value (val [0,1])
    errorP = abs((SimBurntVal - ActualBurntVal) / ActualBurntVal)

    # raw difference
    errorR = (SimBurntVal - ActualBurntVal)
    return errorP, errorR


# Loop Tweaking
for i in range((len(scoreTimeList))):

    # set initial score Time (790 ticks)
    with open('simulateTimeVal.txt', 'r') as timeFile:
        # Read the lines of the file into a list
        tlines = timeFile.readlines()
    # Modify the first line
    tlines[(1 - 1)] = scoreTimeList[i]
    # Open the file in write mode
    with open('simulateTimeVal.txt', 'w') as timeFile:
        # Write the modified lines to the file
        timeFile.writelines(tlines)
    scoreTime = scoreTimeList[i]

    # initial tweak status
    tweakStatus = False

    while tweakStatus == False:

        # Value modifier

        # initial error values
        errorT = comparer()
        errorP = errorT[0]
        errorR = errorT[1]

        # TWEAK FACTORS
        # tweak specifity factor value
        tweakF = 0.001  # tune: tweakF*10^n for less precision and tweakF*10^(-n) for more precision
        # adjustment factor
        a = 1
        # a = math.sqrt(errorP)
        # ideal error
        errorI = 0.1

        # value modifying
        if errorP > errorI:
            # set tweak Status
            tweakStatus = False

            # get old p0 val
            with open('alexandridisVar.txt', 'r') as varFile:
                lines = varFile.readlines()
                second_line = lines[(2 - 1)]
                second_line = second_line.strip()
            p0old = float(second_line)
            # compute new p0 val
            if errorR > 0:
                p0new = p0old - (tweakF * a)
            else:
                p0new = p0old + (tweakF * a)
            # write new p0 val to Var file
            # Open the file in read mode
            with open('alexandridisVar.txt', 'r') as f:
                # Read the lines of the file into a list
                lines = f.readlines()
            # Modify the second line of the list
            lines[1] = f"{p0new}\n"
            # Open the file in write mode
            with open('alexandridisVar.txt', 'w') as f:
                # Write the modified lines to the file
                f.writelines(lines)
            print("current Error", errorP)
        else:
            # set tweak status
            tweakStatus = True

    print("tweaking done for stage", i)


print("tweaking is completed")










#
#     # Open the file in read mode
#     with open('alexandridisVar.txt', 'r') as f:
#         # Read the lines of the file into a list
#         lines = f.readlines()
#
#     # Modify the second line of the list
#     lines[1] = "0.2\n"
#
#     # Open the file in write mode
#     with open('alexandridisVar.txt', 'w') as f:
#         # Write the modified lines to the file
#         f.writelines(lines)

    # exec(open("paramCountBurnt.py").read())
    # testAcreBurnt = countburnt()

    # print(testAcreBurnt)


