import numpy as np


class Genome:
    nV = 3
    v = np.zeros((nV, 2))

    def __init__(self, nV):
        self.nV = nV
        self.v = np.zeros((nV, 2))
