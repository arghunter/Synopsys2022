# alexandridis model burn parameters
# from userInfo import *
import math


with open('alexandridisVar.txt', 'r') as varFile:
    lines = varFile.readlines()

    second_line = lines[(2 - 1)]
    second_line = second_line.strip()

    fifth_line = lines[(5 - 1)]
    fifth_line = fifth_line.strip()

    eighth_line = lines[(8 - 1)]
    eighth_line = eighth_line.strip()

    eleventh_line = lines[(11 - 1)]
    eleventh_line = eleventh_line.strip()

    fourteenth_line = lines[(14 - 1)]
    fourteenth_line = fourteenth_line.strip()

    seventeenth_line = lines[(17 - 1)]
    seventeenth_line = seventeenth_line.strip()

    twentyfirst_line = lines[(21 - 1)]
    twentyfirst_line = twentyfirst_line.strip()


p0 = float(second_line)
c1 = float(fifth_line)
c2 = float(eighth_line)

a = float(eleventh_line)
b = float(fourteenth_line)
d = float(seventeenth_line)


# altitude factor
asubs = float(twentyfirst_line)

def alexandridisModelProbability(thetaf, thetaw, mgw, pveg, pden, h, rthetaS, Mx):
    # calculation of p0

    # tick length (minutes)
    t = 1

    # R0 original is in m/m, convert to m/s then apply formula
    # p0 = (p0tuneVal*((R0 * (1/60)) * ((60*t)/lcell)))
    # p0 must be constant


    # wind direction relative to fire spread direction - thetawf
    thetawf = (thetaw - thetaf)
    rthetawf = abs(math.radians(thetawf))
    # print("relative wind direction", thetawf)

    # U, wind speed (m/s)
    U = (mgw)

    # slope influenced probability
    ps = math.exp((asubs * rthetaS))
    # ps = Rs/R0s # ditch this

    # print("ps", ps)

    # wind influenced probability
    pw = ((math.exp((U * (c1 + (c2 * ((math.cos(rthetawf)) - 1)))))))
    # print("wind influenced prob", pw)

    # moisture content: data link: https://www.wfas.net/index.php/national-fuel-moisture-database-moisture-drought-103
    # Cm = 6
    # MxP = Mx * 100
    #
    # # threshold with extinction fuel moisture
    # if MxP <= Cm:
    #      pm = 0
    # else:
    #      # moisture probability
    #      pm = a * math.exp(((-1) * b * Cm))
    #
    # # height probability
    # ph = (((h/3.281))**d)

    # burn probability
    # with moisture
    # pburn = (p0 * (1 + pveg) * (1+pden) * pw * ps * pm * ph)
    # w/o moisture
    pburn = (p0 * (1 + pveg) * (1 + pden) * pw * ps)

    # print("burn p", pburn)

    return pburn
