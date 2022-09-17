from queue import Queue
import numpy as np
# import files and variables
from userInfo import *


class Genome:
    # nVe = 4
    # v = np.zeros((nV, 2))  # y,x

    def __init__(self, nV):
        self.nV = int(nV)
        self.forwards = np.random.random() <= 0.5
        print("ere")
        self.v = np.zeros((self.nV, 2))
        r = sideLength/2.0
        # r = 30

        qoffset = int(np.random.random()*self.nV)
        rant = np.pi/(self.nV*2)

        for i in range(self.nV):
            while True:
                angle = ((np.pi*2)/self.nV)*(i+qoffset) + \
                    (np.random.random()-0.5)*rant
                # angle = ((np.pi*2)/self.nV)*(i+qoffset)
                mag = (3*r/4)/np.cos((np.abs(angle % np.pi/2)*180/np.pi))+r/4

                # mag = r/np.cos((np.abs(angle*180/np.pi) % 90))
                self.v[i][0] = centery + mag*np.sin(angle*180/np.pi)
                self.v[i][1] = centerx + mag*np.cos(angle*180/np.pi)
                # print(str(self.v[i][0])+" "+str(self.v[i][1]))
                if((self.v[i][0] <= centery+r+8 and self.v[i][1] >= centerx-r-8 and self.v[i][0] >= centery-r-8 and self.v[i][1] <= centerx+r+8)) and (i == 0 or (self.v[i][0]-self.v[i-1][0])**2+(self.v[i][1]-self.v[i-1][1])**2 >= ((r/(2*np.pi))/nV))**2:
                    break
                    # def __init__(self, gnme):
                    #     pass

        self.bx = Queue(maxsize=0)
        self.by = Queue(maxsize=0)
        if self.forwards:
            for i in range(nV):
                self.by.put(int(self.v[i][0]))
                self.bx.put(int(self.v[i][1]))
                cx = int(self.v[i][1])
                cy = int(self.v[i][0])
                t = i+1
                if(not(i < nV+1)):
                    t = 0
                print(str(i)+" "+str(t))
                slope = (cy-int(self.v[t][0]))/(cx-int(self.v[t][1]))
                if(abs(slope) > 1):

                    while(int(cy) != int(self.v[t][0])):
                        d = - \
                            int(abs(cy-int(self.v[t][0])) /
                                (cy-int(self.v[t][0])))
                        cx += d/slope
                        cy += d
                        print(str(cx)+" "+str(cy)+" " +
                              str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))

                    while(int(cx) != int(self.v[t][1])):
                        d = int((int(self.v[t][1])-cx) /
                                abs((int(self.v[t][1])-cx)))
                        cx += d
                        print(str(cx)+" "+str(cy)+" " +
                              str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))
                else:

                    while(int(cx) != int(self.v[t][1])):
                        d = - \
                            int(abs(cx-int(self.v[t][1])) /
                                (cx-int(self.v[t][1])))
                        cx += d
                        cy += slope
                        print(str(cx)+" "+str(cy)+" " +
                              str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))

                    while(int(cy) != int(self.v[t][0])):
                        d = int((int(self.v[t][0])-cy) /
                                abs((int(self.v[t][0])-cy)))
                        cy += d
                        print(str(cx)+" "+str(cy)+" " +
                              str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))
        else:
            for i in range(nV):
                self.by.put(int(self.v[nV-1-i][0]))
                self.bx.put(int(self.v[nV-1-i][1]))
                cx = int(self.v[nV-1-i][1])
                cy = int(self.v[nV-1-i][0])
                t = nV-2-i
                if(t < 0):
                    t = nV-1
                print(str(i)+" "+str(t))
                slope = (cy-int(self.v[t][0]))/(cx-int(self.v[t][1]))
                if(abs(slope) > 1):

                    while(int(cy) != int(self.v[t][0])):
                        d = - \
                            int(abs(cy-int(self.v[t][0])) /
                                (cy-int(self.v[t][0])))
                        cx += d/slope
                        cy += d
                        print(str(cx)+" "+str(cy)+" " +
                              str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))

                    while(int(cx) != int(self.v[t][1])):
                        d = int((int(self.v[t][1])-cx) /
                                abs((int(self.v[t][1])-cx)))
                        cx += d
                        print(str(cx)+" "+str(cy)+" " +
                              str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))
                else:

                    while(int(cx) != int(self.v[t][1])):
                        d = - \
                            int(abs(cx-int(self.v[t][1])) /
                                (cx-int(self.v[t][1])))
                        cx += d
                        cy += slope
                        print(str(cx)+" "+str(cy)+" " +
                              str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))

                    while(int(cy) != int(self.v[t][0])):
                        d = int((int(self.v[t][0])-cy) /
                                abs((int(self.v[t][0])-cy)))
                        cy += d
                        print(str(cx)+" "+str(cy)+" " +
                              str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))
        qs = self.bx.qsize()
        for i in range(qs):
            print("("+str(self.bx.get())+","+str(self.by.get())+")")


gnme = Genome(5)
for i in range(4):
    print(str("("+str(gnme.v[i][0]))+","+str(gnme.v[i][1])+")")
