import math

# Rothermel Model Inputs
# use generic values first

###################################################
# Assumed Values

# assume Timber, grass with understory values as outlined by Rothermel


# surface area to volume ratio (dimentionless)

# fuel moisture
# add in future
# ovendry weight

# ratio of fuel moisture to ovendry weight Mf (lb moisture/ lb wood)
Mf = 0.01 # assume - add in future

# dead fuel moisture of extinction (fraction)
Mx = 0.3

# ratio of moistures (Mf/Mx) (max 1.0)
rm = (Mf/Mx)

# Surface-area-to-volume ratio of tree (ft^2/ft^3) assume Pinus Ponderosa
sigma = 1500 # assume - add real in future

# fuel bed depth (ft)
delta = 1.5

# low heat content (btu/lb)
h = 8000 # assume

# total mineral content (fraction) (lb minerals/lb wood)
ST = 0.0555

# effective mineral content (fraction) (lb minerals - lb silica/ lb wood)
SE = 0.010


# oven dry fuel load (lb/ft^2)
w0 = 0.023

# oven dry bulk density (lb/ft^3)
rhob = (w0*delta)


# oven dry particle density (lb/ft^3) always constant
rhop = 32


#########################################


# Calculated Values

# packing ratio (dimentionless)
# beta = 0.02009 # assume - add in future
beta = (rhob/rhop)

# The energy per unit mass required for ignition is the heat of preignition, Qig:
Qig = (250 + (1116 * Mf))

# propogating flux ratio (dimentionless) xi
xi =((math.exp(((0.792 + (0.681*((sigma)**0.5)))*(beta + 0.1))))/(192+(0.2595*sigma)))


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

# net fuel load (lb/ft^2)
wn = (w0*(1-ST))

# moisture dampening coefficient
etaM = (((1)-(2.59*rm))+(5.11*(rm**2))-(3.51*(rm**3)))

# mineral dampening coefficient (max 1.0)
etaS = (0.174*(1/(SE**0.19)))

# reaction intensity (btu/ft^2 -min)
IR = (gammaprime*h*etaM*etaS)

# wind constants based on sigma
windC = (7.47*(math.exp(((-0.133)*(sigma**0.55)))))
windB = (0.02526 * (sigma**0.54))
windE = (0.715 * (math.exp((-3.59*(1/(10**4)))*sigma)))

########################################################

def rothermelRate(Phi, U):
    # tan Phi - make sure
    phiS = (5.275*(1/(beta**0.3))*(((math.tan(Phi))**2)))

    # phiW wind
    phiW = (windC*(U**windB)*(1/((beta/betaOP)**windE)))

    # rate of spread in feet/min

    # albini extension
    if U >= 0:
        if Phi >= 0:
            Rftmin = ((IR * xi * (1 + phiS + phiW)) / (rhob * epsilon * Qig))
        elif Phi < 0:
            Rftmin = ((IR * xi * (1 + (max(0, (phiW - phiS))))) / (rhob * epsilon * Qig))
    elif U < 0:
        if Phi >= 0:
            Rftmin = ((IR * xi * (1 + (max(0, (phiS - phiW))))) / (rhob * epsilon * Qig))
        elif Phi < 0:
            Rftmin = (((IR * xi)) / (rhob * epsilon * Qig))

    # unit conversion
    Rmh = (Rftmin*18.288)
    Rmm = (Rmh / 60)
    # Rkmh = (Rmh/1000)

    # print("Rothermel rate, meters per min", Rmm)
    return Rmm
