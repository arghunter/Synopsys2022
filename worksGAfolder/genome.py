from queue import Queue
import numpy as np
import random

# import files and variables
from userInfo import *


class Genome:
    # nVe = 4
    # v = np.zeros((nV, 2))  # y,x

    def __init__(self, nV, gnme1=None, gnme2=None,split=-1):
        # print("yCalled")
        self.nV = int(nV)
        if(split == -1):
            self.forwards = np.random.random() <= 0.5
            # print("ere")
            self.v = np.zeros((self.nV, 2))
            r = (sideLength/2.0)
      
            # r = 60
            # r = 30

            qoffset = int(np.random.random()*self.nV)
            self.qoffset=qoffset
            rant = np.pi/(self.nV)

            for i in range(self.nV):
                while True:
                    angle = ((np.pi*2)/(self.nV))*(i+qoffset) + \
                        (np.random.random()*rant)

                    # angle = ((np.pi*2)/self.nV)*(i+qoffset)

                    # mag = abs(
                    #     (3*r/4)/np.cos((np.abs(angle % np.pi/2)*180/np.pi))+r/4)
                    mag = 0
                    if(angle % np.pi/2 == 0):
                        mag = r
                    else:
                        mag = (r+(np.sqrt(r**2+(np.tan(angle)*r)**2) *
                                  ((np.random.random()-0.6)+0.6)))/2
                    # mag = r
                    # mag = abs(r*np.sqrt(2)*np.tan((angle)*180/np.pi))
                    # print(mag)
                    # print(angle*180/np.pi)
                    # print(np.sin(angle))
                    # mag = r/np.cos((np.abs(angle*180/np.pi) % 90))
                    self.v[i][0] = centery + mag*(np.sin(angle))
                    self.v[i][1] = centerx + mag*(np.cos(angle))
                    # print(str(self.v[i][0])+" "+str(self.v[i][1]))
                    if((self.v[i][0] <= centery+r+8 and self.v[i][1] >= centerx-r-8 and self.v[i][0] >= centery-r-8 and self.v[i][1] <= centerx+r+8)) and (i == 0 or (self.v[i][0]-self.v[i-1][0])**2+(self.v[i][1]-self.v[i-1][1])**2 >= ((r/(2*np.pi))/nV))**2:
                        break
                        # def __init__(self, gnme):
                        #     pass
        else:
            self.forwards = gnme1.forwards
            # print("ere")
            self.v = np.zeros((self.nV, 2))

            # r = 60
            # r = 30
            self.qoffset=gnme1.qoffset
            for i in range(split):
                self.v[i][0] = gnme1.v[i][0]
                self.v[i][1] = gnme1.v[i][1]
            toffset=gnme1.qoffset-gnme2.qoffset
            for i in range(split,nV):
                ti=i+toffset
                if(ti<0):
                    ti=nV+toffset
                elif(ti>=nV):
                    ti-=nV
                self.v[i][0] = gnme2.v[ti][0]
                self.v[i][1] = gnme2.v[ti][1]
                if(np.random.random()<0.028):
                    self.v[i][0] = self.v[i][0]+(np.random.random()-0.5)*sideLength
                    self.v[i][1] = self.v[i][1]+(np.random.random()-0.5)*sideLength
                    
                

        self.bx = Queue(maxsize=0)
        self.by = Queue(maxsize=0)
        if self.forwards:
            for i in range(nV):
                self.by.put(int(self.v[i][0]))
                self.bx.put(int(self.v[i][1]))
                cx = int(self.v[i][1])
                cy = int(self.v[i][0])
                t = i+1
                if(not(i < nV-1)):
                    t = 0
                # print(str(i)+" "+str(t))
                if(cx == int(self.v[t][1])):
                    slope = 0
                else:
                    slope = (cy-int(self.v[t][0]))/(cx-int(self.v[t][1]))

                if(abs(slope) > 1):
                    lx = cx
                    while(int(cy) != int(self.v[t][0])):
                        d = - \
                            int(abs(cy-int(self.v[t][0])) /
                                (cy-int(self.v[t][0])))
                        # print(str(cx)+" "+str(cy)+" "+str(lx))

                        cx += d/slope
                        if(abs(int(cx)-lx) >= 1):
                            # print(str(cx)+" "+str(cy)+" "+str(lx)+"2")
                            self.bx.put(int(cx))
                            self.by.put(int(cy))
                            lx = int(cx)
                        cy += d
                        # print(d/slope)
                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))

                        self.bx.put(int(cx))
                        self.by.put(int(cy))

                    while(int(cx) != int(self.v[t][1])):
                        d = int((int(self.v[t][1])-cx) /
                                abs((int(self.v[t][1])-cx)))
                        cx += d
                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))
                else:
                    ly = cy
                    while(int(cx) != int(self.v[t][1])):
                        d = - \
                            int(abs(cx-int(self.v[t][1])) /
                                (cx-int(self.v[t][1])))
                        # print(str(cx)+" "+str(cy)+" "+str(ly))
                        cy += slope

                        if abs(ly-int(cy)) >= 1:
                            # print(str(cx)+" "+str(cy)+" "+str(ly)+"2")

                            self.bx.put(int(cx))
                            self.by.put(int(cy))
                            ly = int(cy)
                        cx += d

                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))

                    while(int(cy) != int(self.v[t][0])):
                        d = int((int(self.v[t][0])-cy) /
                                abs((int(self.v[t][0])-cy)))
                        cy += d
                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
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
                # print(str(i)+" "+str(t))
                if(cx == int(self.v[t][1])):
                    slope = 0
                else:
                    slope = (cy-int(self.v[t][0]))/(cx-int(self.v[t][1]))

                if(abs(slope) > 1):
                    lx = cx
                    while(int(cy) != int(self.v[t][0])):
                        d = - \
                            int(abs(cy-int(self.v[t][0])) /
                                (cy-int(self.v[t][0])))
                        # print(str(cx)+" "+str(cy)+" "+str(lx))

                        cx += d/slope

                        if(abs(int(cx)-lx) >= 1):
                            # print(str(cx)+" "+str(cy)+" "+str(lx)+"2")
                            self.bx.put(int(cx))
                            self.by.put(int(cy))
                            lx = int(cx)
                        cy += d
                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))

                    while(int(cx) != int(self.v[t][1])):
                        d = int((int(self.v[t][1])-cx) /
                                abs((int(self.v[t][1])-cx)))
                        cx += d
                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))
                else:
                    ly = cy
                    while(int(cx) != int(self.v[t][1])):
                        d = - \
                            int(abs(cx-int(self.v[t][1])) /
                                (cx-int(self.v[t][1])))
                        # print(str(cx)+" "+str(cy)+" "+str(ly))

                        cy += slope
                        if abs(ly-int(cy)) >= 1:
                            # print(str(cx)+" "+str(cy)+" "+str(ly)+"2")
                            self.bx.put(int(cx))
                            self.by.put(int(cy))
                            ly = int(cy)
                        cx += d
                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))

                    while(int(cy) != int(self.v[t][0])):
                        d = int((int(self.v[t][0])-cy) /
                                abs((int(self.v[t][0])-cy)))
                        cy += d
                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))


#         qs = self.bx.qsize()
#         for i in range(qs):
#             print("("+str(self.bx.get())+","+str(self.by.get())+")")


# gnme = Genome(12)
# for i in range(12):
#     print(str("("+str(gnme.v[i][1]))+","+str(gnme.v[i][0])+")")
