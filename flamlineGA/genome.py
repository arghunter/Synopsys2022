import numpy as np
# import files and variables
from userInfo import *


class Genome:
    # nVe = 4
    # v = np.zeros((nV, 2))  # y,x

    def __init__(self, nV):
        self.nV = int(nV)
        print("ere")
        self.v = np.zeros((self.nV, 2))
        r = sideLength/2.0
        # r = 30

        qoffset = int(np.random.random()*self.nV)
        rant = np.pi/self.nV
        for i in range(self.nV):
            while True:
                angle = ((np.pi*2)/self.nV)*(i+qoffset) + \
                    (np.random.random()-0.5)*rant
                mag = (3*r/4)/np.cos((np.abs(angle*180/np.pi) % 90))+r/4

                mag = r/np.cos((np.abs(angle*180/np.pi) % 90))
                self.v[i][0] = centery + mag*np.sin(angle*180/np.pi)
                self.v[i][1] = centerx + mag*np.cos(angle*180/np.pi)
                # print(str(self.v[i][0])+" "+str(self.v[i][1]))
                if((self.v[i][0] <= centery+r+5 and self.v[i][1] >= centerx-r-5 and self.v[i][0] >= centery-r-5 and self.v[i][1] <= centerx+r+5)):
                    break

    # def __init__(self, gnme):
    #     pass


gnme = Genome(10)
for i in range(10):
    print(str(gnme.v[i][0])+" "+str(gnme.v[i][1])+")")
