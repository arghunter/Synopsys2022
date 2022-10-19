from queue import Queue
import numpy as np
import random

# import files and variables
from data import *


class Genome:
    # nVe = 4
    # v = np.zeros((nV, 2))  # y,x
    fwidth=4
    def __init__(self, nV,data,ignitionX,ignitionY, gnme1=None, gnme2=None,split=-1):
        """
        It takes a list of vertices and creates a queue of points that are the vertices and the points
        between the vertices.
        
        :param nV: number of vertices
        :param data: the image
        :param ignitionX: The x coordinate of the ignition point
        :param ignitionY: The y coordinate of the ignition point
        :param gnme1: The first genome to be used in the crossover
        :param gnme2: the second genome
        :param split: the number of vertices to take from the first genome
        """
        # print("yCalled")
        self.nV = int(nV)
        self.ignitionX = ignitionX
        self.ignitionY = ignitionY
        if(split == -1):
            self.forwards = np.random.random() <= 0.5
            # print("ere")
            self.v = np.zeros((self.nV, 2))
            r = (min(data.ncols,data.nrows)/2.0)
      
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
                    self.v[i][0] = ignitionY + mag*(np.sin(angle))
                    self.v[i][1] = ignitionX+ mag*(np.cos(angle))
                    # print(str(self.v[i][0])+" "+str(self.v[i][1]))
                   
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
                    self.v[i][0] = self.v[i][0]+(np.random.random()-0.5)*r*2
                    self.v[i][1] = self.v[i][1]+(np.random.random()-0.5)*r*2
                    
                

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
                        d*=Genome.fwidth
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
                        d*=Genome.fwidth
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
                        d*=Genome.fwidth
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
                        d*=Genome.fwidth
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
                        d*=Genome.fwidth
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
                        d*=Genome.fwidth
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
                        d*=Genome.fwidth
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
                        d*=Genome.fwidth
                        cy += d
                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))
    #data  current tick  spt=fwitdhpertick
    def getFitness(self,data,tick,spt):
        
        pass
    #data  
    def floodFill(self,data,y,x,burnt):
        if(x<=0 or y<=0 or y>data.nrows-1 or x>data.ncols-1 or data.BURN[y][x][1]==0):
            return
        burnt[0]+=1
        self.floodFill(data,y+1,x,burnt)
        self.floodFill(data,y-1,x,burnt)
        self.floodFill(data,y,x+1,burnt)
        self.floodFill(data,y,x-1,burnt)
        self.floodFill(data,y-1,x-1,burnt)
        self.floodFill(data,y+1,x-1,burnt)
        self.floodFill(data,y-1,x+1,burnt)
        self.floodFill(data,y+1,x+1,burnt)
        
        
            
             
             
        
        
        
        
        
#         qs = self.bx.qsize()
#         for i in range(qs):
#             print("("+str(self.bx.get())+","+str(self.by.get())+")")


# gnme = Genome(12)
# for i in range(12):
#     print(str("("+str(gnme.v[i][1]))+","+str(gnme.v[i][0])+")")
