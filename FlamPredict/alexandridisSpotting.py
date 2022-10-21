import numpy as np
from numpy import random
import math

lambdaVal = 1  # lambda for poisson for Number of spotting items #TODO: find value

rnMeanVal = 5  # mean val for rn from gaussian dist #TODO: find val
rnStdVal = 5  # std val for rn from gaussian dist #TODO: find val

def alexandridisSpotting():
    # spotting

    Nsubp = int(random.poisson(lam=lambdaVal, size=None))  # number of spotting cells from poisson dist
    # info: size= None gives one scalar value

    # spotting distance

    # generated random rn from gaussian distribution
    rsubn = float(random.normal(loc=rnMeanVal, scale=rnStdVal, size=None))
    # info: size = None gives one scalar value
    # info: loc = mean
    # info: scale = std
