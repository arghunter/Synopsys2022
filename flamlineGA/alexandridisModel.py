# alexandridis model burn parameters
from userInfo import *
import math

ph = 0.58  # pre optimised

# p veg dependent on land type - pre defined by alexandridis
# land types, 1 - forest, 2 - shrubs, 3 - agriculture, 4 - no vegetation
if landType == 1:
    pveg = 0.4
elif landType == 2:
    pveg = 0.4
elif landType == 3:
    pveg = -0.4
elif landType == 4:
    pveg = -1

# p veg dependent on land type - pre defined by alexandridis
# den types, 1 - dense, 2 - normal, 3 - sparse, 4 - no vegetation
if denType == 1:
    pden = 0.3
elif denType == 2:
    pden = 0
elif denType == 3:
    pden = -0.3
elif denType == 4:
    pden = -1

# pre determined by optimization
c1 = 0.045
c2 = 0.131

# altitude factor
a = 0.078

# wind velocity at midflame height (squares per tick) # TODO: when add wind data convert m/min to squares/ tick
U = 5

# wind direction (deg)
thetaw = 225


def alexandridisModelProbability(dthetaS, thetaf):
    # wind direction relative to fire spread direction - thetawf
    thetawf = (thetaw - thetaf)
    print("relative wind direction", thetawf)

    # slope influenced probability
    ps = math.exp((a * dthetaS))
    print("ps", ps)

    # wind influenced probability parameter
    fsubt = math.exp((U * c2 * ((math.cos(thetawf)) - 1)))

    # wind influenced probability
    pw = ((fsubt * math.exp((c1 * U))))
    print("wind influenced prob", pw)


    # burn probability
    pburn = (ph * (1 + pveg) * (1+pden) * pw * ps)

    return pburn

