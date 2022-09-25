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

fireSpreadSpeed = int(4*scaleVal)
lineDrawSpeed = int(40*scaleVal)
userDelay = int(20*scaleVal)
bufferSpace = int(20*scaleVal)

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

# Rothermel Model Inputs
# use generic values first

# assume TU5: Very High Load, Dry Climate Timber-Shrub

# packing ratio (dimentionless)
beta = 0.02009



# Moisture Damping Coefficient from [0,1]
# etaM =
# Mineral Damping Coefficient from [0,1]
# etaS =
# Potential Reaction Velocity (min^-1)
# gammaPrime =


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


