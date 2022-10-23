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
Mf = 0.01  # assume - add in future

# dead fuel moisture of extinction (fraction)
# MxSpot = 0.3 # dead fuel moisture of extinction (fraction)

# # ratio of moistures (Mf/MxSpot) (max 1.0)
# rm = (Mf / MxSpot)

# Surface-area-to-volume ratio of tree (ft^2/ft^3) assume Pinus Ponderosa
# sigmaSpot = 1500  # assume - add real in future
# sigmaSpot = 0 # Surface-area-to-volume ratio of tree (ft^2/ft^3)

# fuel bed depth (ft)
# deltaSpot = 1.5 # fuel bed depth (ft)

# low heat content (btu/lb)
# h = 8000  # assume

# total mineral content (fraction) (lb minerals/lb wood)
ST = 0.0555

# effective mineral content (fraction) (lb minerals - lb silica/ lb wood)
SE = 0.010

# oven dry fuel load (lb/ft^2)
# w0Spot = 0.023 # oven dry fuel load (lb/ft^2)

# # oven dry bulk density (lb/ft^3)
# rhob = (w0Spot * deltaSpot)

# oven dry particle density (lb/ft^3) always constant
# rhop = 32

#########################################


# Calculated Values

# # packing ratio (dimentionless)
# # betaSpot = 0.02009 # assume - add in future
# betaSpot = (rhob / rhop)
#
# # The energy per unit mass required for ignition is the heat of preignition, Qig:
# Qig = (250 + (1116 * Mf))
#
# # propogating flux ratio (dimentionless) xi
# xi = ((math.exp(((0.792 + (0.681 * ((sigmaSpot) ** 0.5))) * (betaSpot + 0.1)))) / (192 + (0.2595 * sigmaSpot)))
#
# # effective heating number
# epsilon = ((math.exp((-138 / sigmaSpot))))
#
# # Maximum reaction velocity (min^-1)
# gammaprimeMax = (((sigmaSpot ** 1.5)) / (495 + (0.0594 * (sigmaSpot ** 1.5))))
#
# # A coefficient for optimum reaction velocity
# A = (133 * (1 / (sigmaSpot ** 0.7913)))
#
# # optimum packing ratio
# betaSpotOP = (3.348 * (1 / (sigmaSpot ** 0.8189)))
#
# # optimum reaction velocity (min^-1)
# gammaprime = ((gammaprimeMax * ((betaSpot / betaSpotOP) ** A)) * (math.exp((A * (1 - (betaSpot / betaSpotOP))))))
#
# # net fuel load (lb/ft^2)
# wn = (w0Spot * (1 - ST))
#
# # moisture dampening coefficient
# etaM = (((1) - (2.59 * rm)) + (5.11 * (rm ** 2)) - (3.51 * (rm ** 3)))
#
# # mineral dampening coefficient (max 1.0)
# etaS = (0.174 * (1 / (SE ** 0.19)))
#
# # reaction intensity (btu/ft^2 -min)
# IR = (gammaprime * h * etaM * etaS)
#
# # wind constants based on sigmaSpot
# windC = (7.47 * (math.exp(((-0.133) * (sigmaSpot ** 0.55)))))
# windB = (0.02526 * (sigmaSpot ** 0.54))
# windE = (0.715 * (math.exp((-3.59 * (1 / (10 ** 4))) * sigmaSpot)))


########################################################

def rothermelRateSpot(tanPhiSpot, realUSpot, hSpot, deltaSpot, betaSpot, MxSpot, w0Spot, sigmaSpot):
    # ratio of moistures (Mf/MxSpot) (max 1.0)
    rm = (Mf / MxSpot)

    # oven dry bulk density (lb/ft^3)
    rhob = (w0Spot * deltaSpot)

    # packing ratio (dimentionless)
    # betaSpot = 0.02009 # assume - add in future
    # betaSpot = (rhob / rhop)


    # The energy per unit mass required for ignition is the heat of preignition, Qig:
    Qig = (250 + (1116 * Mf))

    # propogating flux ratio (dimentionless) xi
    xi = ((math.exp(((0.792 + (0.681 * ((sigmaSpot) ** 0.5))) * (betaSpot + 0.1)))) / (192 + (0.2595 * sigmaSpot)))

    # effective heating number
    epsilon = ((math.exp((-138 / sigmaSpot))))

    # Maximum reaction velocity (min^-1)
    gammaprimeMax = (((sigmaSpot ** 1.5)) / (495 + (0.0594 * (sigmaSpot ** 1.5))))

    # A coefficient for optimum reaction velocity
    A = (133 * (1 / (sigmaSpot ** 0.7913)))

    # optimum packing ratio
    betaSpotOP = (3.348 * (1 / (sigmaSpot ** 0.8189)))

    # optimum reaction velocity (min^-1)
    gammaprime = ((gammaprimeMax * ((betaSpot / betaSpotOP) ** A)) * (math.exp((A * (1 - (betaSpot / betaSpotOP))))))

    # net fuel load (lb/ft^2)
    wn = (w0Spot * (1 - ST))

    # moisture dampening coefficient
    etaM = (((1) - (2.59 * rm)) + (5.11 * (rm ** 2)) - (3.51 * (rm ** 3)))

    # mineral dampening coefficient (max 1.0)
    etaS = (0.174 * (1 / (SE ** 0.19)))

    # reaction intensity (btu/ft^2 -min)
    IR = (gammaprime * hSpot * etaM * etaS)

    # wind constants based on sigmaSpot
    windC = (7.47 * (math.exp(((-0.133) * (sigmaSpot ** 0.55)))))
    windB = (0.02526 * (sigmaSpot ** 0.54))
    windE = (0.715 * (math.exp((-3.59 * (1 / (10 ** 4))) * sigmaSpot)))

    # tan Phi - make sure

    phiS = (5.275 * (1 / (betaSpot ** 0.3)) * (((tanPhiSpot) ** 2)))

    # phiW wind
    phiW = (windC * (realUSpot ** windB) * (1 / ((betaSpot / betaSpotOP) ** windE)))

    # rate of spread in feet/min

    # albini extension
    if realUSpot >= 0:
        if tanPhiSpot >= 0:
            RftminSpot = ((IR * xi * (1 + phiS + phiW)) / (rhob * epsilon * Qig))
        elif tanPhiSpot < 0:
            RftminSpot = ((IR * xi * (1 + (max(0, (phiW - phiS))))) / (rhob * epsilon * Qig))
    elif realUSpot < 0:
        if tanPhiSpot >= 0:
            RftminSpot = ((IR * xi * (1 + (max(0, (phiS - phiW))))) / (rhob * epsilon * Qig))
        elif tanPhiSpot < 0:
            RftminSpot = (((IR * xi)) / (rhob * epsilon * Qig))

    RmhSpot = (RftminSpot * 18.288)
    RmmSpot = ((RmhSpot / 60))
    # Rkmh = (Rmh/1000)

    # print("Rothermel rate, meters per min", Rmm)
    return RmmSpot