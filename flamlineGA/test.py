import numpy as np
from userInfo import *


class Genome:

    # init method or constructor
    def __init__(self, nV):
        self.nV = int(nV)
        # print("ere")
        self.v = np.zeros((self.nV, 2))
        # r = sideLength/2.0
        r = 30

        qoffset = int(np.random.random()*self.nV)
        rant = np.pi*2/self.nV
        for i in range(self.nV):
            while True:
                angle = ((np.pi*2)/self.nV)*(i+qoffset) + \
                    (np.random.random()-0.5)*rant
                mag = r/np.cos((np.abs(angle*180/np.pi) % 90))
                self.v[i][0] = centery + mag*np.sin(angle*180/np.pi)
                self.v[i][1] = centerx + mag*np.cos(angle*180/np.pi)
                print(str(self.v[i][0])+" "+str(self.v[i][1]))
                if((self.v[i][0] <= centery+r+5 and self.v[i][1] >= centerx-r-5 and self.v[i][0] >= centery-r-5 and self.v[i][1] <= centerx+r+5)):
                    break


# Creating different objects
p1 = Genome(8)
p2 = Genome(4)
p3 = Genome(3)
print(p2.v)

# p1.say_hi()
# p2.say_hi()
# p3.say_hi()
