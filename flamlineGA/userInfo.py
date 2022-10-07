import math

########################################################

# set values here

# nx and ny must be multiples of 1024
nx = 1024
ny = 1024
landSideLength = int(nx)
rlandSideLength = int(landSideLength - 1)

# for nx = 1024, squareSize = 20m --> squareSize = nx * (20/1024)
squareSize = int(nx * (20/1024))
scaleVal = int(squareSize/20)

fireSpreadSpeed = int(1*scaleVal)
lineDrawSpeed = int(10*scaleVal)
userDelay = int(20*scaleVal)
bufferSpace = int(20*scaleVal)

forest_fraction = 0.85
altitude_vari = 0.5
p, f = 0.85, 0.01
# spread_chance = 0.4
centerx = nx/2
centery = ny/2
vertexNum = 10

maxGenerations = 2
intmaxGenerations = int(maxGenerations)
maxPopSize = 2
intmaxPopSize = int(maxPopSize)

# land types, 1 - forest, 2 - agriculture, 3 - rivers, 4 - roads
landType = 1

##################################################################

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
