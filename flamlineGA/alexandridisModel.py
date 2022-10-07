# alexandridis model burn parameters
from userInfo import *
import math

ph = 0.58  # pre optimised

# p veg dependent on land type - pre defined by alexandridis
if landType == 1:
    pveg = 0.4
elif landType == 2:
    pveg = -0.3
elif landType == 3:
    pveg = -0.7
elif landType == 4:
    pveg = -0.5

# pre determined by optimization
c1 = 0.045
c2 = 0.131

# altitude factor
a = 0.078

# wind velocity at midflame height (m/min)
U = 0

# wind direction (deg)
thetaw = 45


def alexandridisModelProbability(thetaS, thetaf):
    # wind direction relative to fire spread direction - thetawf
    thetawf = thetaw - thetaf

    # slope influenced probability
    ps = math.exp(a * thetaS)

    # wind influenced probability parameter
    fsubt = math.exp(U * c2 * ((math.cos(thetawf)) - 1))

    # wind influenced probability
    pw = (fsubt * math.exp(c1 * U))

    # burn probability
    pburn = (ph * (1 + pveg) * pw * ps)

    return pburn

