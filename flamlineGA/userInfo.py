import math

########################################################

# set values here

fireSpreadSpeed = 4
lineDrawSpeed = 40
userDelay = 20
bufferSpace = 20
nx = 1024
ny = 1024
forest_fraction = 0.95
altitude_vari = 0.5
p, f = 0.85, 0.01
spread_chance = 0.4
centerx = nx/2
centery = ny/2
vertexNum = 10
maxGenerations = 2
intmaxGenerations = int(maxGenerations)

maxPopSize = 2
intmaxPopSize = int(maxPopSize)

# set values here

########################################################

iFSS = float(fireSpreadSpeed)

# iFSSC = Number of Ticks in a Minute (because 1 square every tick)
iFSSC = int((iFSS * 1000) / 20)
# ms per tick
tickRATE = (60 / iFSSC) * 1000
iTR = int(tickRATE)

# line draw speed
iLDS = int(lineDrawSpeed)
iLDSS = (iLDS * 1000) / 20
# fireline draw speed in squares per tick = iLDSST
iLDSST = iLDSS / iFSSC

iUD = int(userDelay)
iBS = int(bufferSpace)

Tau = ((((4 * iUD) / iLDSST) + ((4 * iBS) / iLDSST) + iBS) / ((1 - (4 / iLDSST))))
upTau = math.ceil(Tau)

# Tau = sidelength value because square = tick
sideLength = ((upTau + iUD + iBS))
