import math

########################################################

# set values here

fireSpreadSpeed = 2
lineDrawSpeed = 10
userDelay = 20
bufferSpace = 20

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

iTau = ((((4 * iUD) / iLDSST) + ((4 * iBS) / iLDSST) + iBS) / ((1 - (4 / iLDSST))))
upTau = math.ceil(iTau)

# Tau = sidelength value because square = tick
sideLength = ((upTau + iUD + iBS))

