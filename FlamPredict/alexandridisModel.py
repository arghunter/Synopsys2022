# alexandridis model burn parameters
# from userInfo import *
import math


p0 = 0.72
c1 = 0.045
c2 = 0.191

a = 2.5
b = 0.15
d = 0.932


# altitude factor
asubs = 0.088

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
    Cm = 6.9
    MxP = Mx * 100
    #
    # threshold with extinction fuel moisture
    if MxP <= Cm:
        pm = 0
    else:
        # moisture probability
        pm = a * math.exp(((-1) * b * Cm))
    #
    # height probability
    ph = (((h/3.281))**d)

    # burn probability
    # with moisture
    # pburn = (p0 * (1 + pveg) * (1+pden) * pw * ps * pm * ph)
    # w/o moisture
    pburn = (p0 * (1 + pveg) * (1 + pden) * pw * ps * ph * pm)

    # print("burn p", pburn)

    return pburn
