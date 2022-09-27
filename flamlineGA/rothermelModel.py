import math

# Rothermel Model Inputs
# use generic values first

###################################################
# Assumed Values

# assume TU5: Very High Load, Dry Climate Timber-Shrub

# packing ratio (dimentionless)
beta = 0.02009 # assume - add in future

# surface area to volume ratio (dimentionless)

# fuel moisture
# add in future
# ovendry weight

# ratio of fuel moisture to ovendry weight Mf (lb moisture/ lb wood)
Mf = 0.05 # assume - add in future

# Surface-area-to-volume ratio of tree (ft^2/ft^3) assume Pinus Ponderosa
sigma = 12.4968 # assume - add real in future

# fuel bed depth (ft)
delta = 0.3375

# low heat content (btu/lb)
h = 8000 # assume

# total mineral content (fraction) (lb minerals/lb wood)
ST = 0.0555

# effective mineral content (fraction) (lb minerals - lb silica/ lb wood)
SE = 0.010

# oven dry particle density (lb/ft^3)
rhop = 32

# oven dry fuel load (lb/ft^2)
w0 = 28.65

# wind velocity at midflame height (ft/min)
U = 0

#########################################


# Calculated Values


# The energy per unit mass required for ignition is the heat of preignition, Qig:
Qig = (250 + (1116 * Mf))

# propogating flux ratio (dimentionless) xi
xi =((math.exp(((0.792 + (0.681*((sigma)**0.5)))*(beta + 0.1))))/(192+(0.2595*sigma)))

# oven dry bulk density (lb/ft^3)
rhob = (beta * rhop)

# effective heating number
epsilon = ((math.exp((-138/sigma))))

# Maximum reaction velocity (min^-1)
gammaprimeMax = (((sigma**1.5))/(495+(0.0594*(sigma**1.5))))

# A coefficient for optimum reaction velocity
A = (133*(1/(sigma**0.7913)))

# optimum packing ratio
betaOP = (3.348*(1/(sigma**0.8189)))

# optimum reaction velocity (min^-1)
gammaprime = ((gammaprimeMax*((beta/betaOP)**A))*(math.exp((A*(1-(beta/betaOP))))))



########################################################
