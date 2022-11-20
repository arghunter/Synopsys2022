from queue import Queue
import numpy as np
import random

# import files and variables
from data import *


class FireLine:
    # nVe = 4
    # v = np.zeros((nV, 2))  # y,x

    def __init__(self, v,nV):
        # print("yCalled")
        self.nV = nV;
        self.v=v
        self.avgX=0;
        for i in v:
            self.avgX+=i[0]
            self.avgY+=i[1]
        self.avgX/=self.nV
        self.avgY/=self.nV
        self.forwards = np.random.random() <= 0.5
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
                            
                            self.bx.put(int(cx))
                            self.by.put(int(cy))
                            lx = int(cx)
                        cy += d
                        

                        self.bx.put(int(cx))
                        self.by.put(int(cy))

                    while(int(cx) != int(self.v[t][1])):
                        d = int((int(self.v[t][1])-cx) /
                                abs((int(self.v[t][1])-cx)))
                        cx += d
                        
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
                        
    def floodFill(self,data,X,rx,ry,sms):
        
        q=Queue(0)
        q.put((rx,ry))
        size=0
        
        while(not q.empty()):
            p=q.get()
            rx=p[0]
            ry=p[1]
            
            if not(not(rx  >= 0 and ry  >= 0 and ry< data.nrows and rx  < data.ncols) or data.X[ry][rx]!=0 ):
                
                size+=1
                # print(str(data.COLORS[ry][rx])+" "+ str(ry)+" "+str(rx)+" "+str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2))
                X[ry][rx]=1
                q.put((rx+1,ry))
                q.put((rx-1,ry))
                q.put((rx,ry+1))
                q.put((rx,ry+1))
                q.put((rx+1,ry+1))
                q.put((rx+1,ry-1))
                q.put((rx-1,ry-1))
                q.put((rx-1,ry+1))
        return size
                
  
        
    def getScore(self,data,buffer,time,speedms,X):
        qs=self.bx.qsize()
        scoreW=1000;
        while(qs>0):
            rx=self.bx.get();
            ry=self.by.get();
            X[ry][rx]=-1;
            self.bx.put(rx)
            self.by.put(ry)
        score=self.floodFill(data,X,int(self.avgX),int(self.avgY))
        
        
            
        lx=self.bx.get();
        ly=self.by.get();
        for i in range(6):
            for j in range(6):
                if(ly-3+i>=0 and ly-3+i<data.nrows and lx-3+j>=0 and lx-3+j<data.ncols  ):
                    if(data.BURN[ly-3+i][lx-3+j]<time+buffer and not (X[ly-3+i][lx-3+j]==2)):
                        score+=scoreW
                        X[ly-3+i][lx-3+j]=2
        
        while(not self.bx.empty()):
            rx=self.bx.get();
            ry=self.by.get();
            dy=ry-ly;
            dx=rx-lx;
            d=np.sqrt(dy**2+dx**2)
            time+=d/speedms
            ly=ry
            lx=rx
            for i in range(6):
                for j in range(6):
                    if(ly-3+i>=0 and ly-3+i<data.nrows and lx-3+j>=0 and lx-3+j<data.ncols  ):
                        if(data.BURN[ly-3+i][lx-3+j]<time+buffer and not (X[ly-3+i][lx-3+j]==2)):
                            score+=scoreW
                            X[ly-3+i][lx-3+j]=2
        return score
    
    
class Rectangle:
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.y2=y2
        self.x2=x2
    def intersects(self,other):
        return ((self.x1<=other.x1 and self.x2>=other.x1 or other.x1<=self.x1 and other.x2>=self.x1) and (self.y1<=other.y1 and self.y2>=other.y1 or other.y1<=self.y1 and other.y2>=self.y1))
        
    
class Genome:
    def __init__(self,rects):
        rectrects=[]
        for rect in rects:
            rectrects.appends(Rectangle(rect[0],rect[1],rect[2],rect[3]))
        intsec=[]
        for i in range (len(rects)):
            intsec.append({})
            for j in range(i+1,len(rects)):
                if(rectrects[i].intersects(rectrects[j])):
                    intsec[i].add(j)
        vx=[]
       
    def cycleintsec(rectrects,intsec,vx):
         for i in len(intsec):
            tripped=True
            while(tripped):
                for val in intsec[i]:
                    if(val != -1):
                        x=intsec[i].update(intsec[val])
                        if (x==intsec[i]):
                            tripped=False
                        else:
                            intsec[i]=x
                            intsec[i].add(-1)
                            break
                        #take the sets shove the unique un touched ones that contain -1 into vx and add verts
            
                    
            
            
            
        
            
            
            
            
            
        
                    
        self.lines=[] #list of fire lines
        
    
    
    def floodFill(self,data,X,simtime):
        
        q=Queue(0)
        q.put((rx,ry))
     
        score=0
        while(not q.empty()):
            p=q.get()
            rx=p[0]
            ry=p[1]
            
            if not(not(rx  >= 0 and ry  >= 0 and ry< data.nrows and rx  < data.ncols) or X[ry][rx]==0):
                
                if(data.BURN[ry][rx]>0 and data.BURN[ry][rx]<=simtime):
                    score+=1000
                    
                
                # print(str(data.COLORS[ry][rx])+" "+ str(ry)+" "+str(rx)+" "+str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2))
                X[ry][rx]=1
                q.put((rx+1,ry))
                q.put((rx-1,ry))
                q.put((rx,ry+1))
                q.put((rx,ry+1))
                q.put((rx+1,ry+1))
                q.put((rx+1,ry-1))
                q.put((rx-1,ry-1))
                q.put((rx-1,ry+1))
                
                
    def getFitness(self,data,buffer,time,speedms):
        score=0;
        X=np.zeros(data.COLORS.shape())
            
        for l in self.lines:
            score+=l.getScore(data,buffer,time,speedms)
        for i in data.ncols:
            for j in data.nrows:
                score+=self.floodFill(data,X,i,j)

        
        
        
        
            
        
        
        
             
            
            
            
        
        
