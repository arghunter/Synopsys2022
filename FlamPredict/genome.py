from queue import Queue
import numpy as np
import random
from functools import cmp_to_key
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import time
# from scipy.spatial import Delaunay
# import alphashape
from fire import *
# import files and variables
from data import *


class FireLine:
    # nVe = 4
    # v = np.zeros((nV, 2))  # y,x

    def __init__(self, v, nV):
        # print("yCalled")
        self.nV = nV;
        self.v = v
        self.avgX = 0;
        self.avgY = 0;
        for i in v:
            self.avgX += i[0]
            self.avgY += i[1]
        self.avgX /= self.nV
        self.avgY /= self.nV
        self.forwards = np.random.random() <= 0.5
        self.bx = Queue(maxsize=0)
        self.by = Queue(maxsize=0)
        if self.forwards:
            for i in range(nV):
                self.by.put(int(self.v[i][1]))
                self.bx.put(int(self.v[i][0]))
                cx = int(self.v[i][0])
                cy = int(self.v[i][1])
                t = i+1
                if(not(i < nV-1)):
                    t = 0
                # print(str(i)+" "+str(t))
                if(cx == int(self.v[t][0])):
                    slope = 0
                else:
                    slope = (cy-int(self.v[t][1]))/(cx-int(self.v[t][0]))

                if (abs(slope) > 1):
                    lx = cx
                    while(int(cy) != int(self.v[t][1])):
                        d = - \
                            int(abs(cy-int(self.v[t][1])) /
                                (cy-int(self.v[t][1])))
                        # print(str(cx)+" "+str(cy)+" "+str(lx))

                        cx += d / slope
                        if (abs(int(cx) - lx) >= 1):
                            self.bx.put(int(cx))
                            self.by.put(int(cy))
                            lx = int(cx)
                        cy += d

                        self.bx.put(int(cx))
                        self.by.put(int(cy))

                    while(int(cx) != int(self.v[t][0])):
                        d = int((int(self.v[t][0])-cx) /
                                abs((int(self.v[t][0])-cx)))
                        cx += d

                        self.bx.put(int(cx))
                        self.by.put(int(cy))
                else:
                    ly = cy
                    while(int(cx) != int(self.v[t][0])):
                        d = - \
                            int(abs(cx-int(self.v[t][0])) /
                                (cx-int(self.v[t][0])))
                        # print(str(cx)+" "+str(cy)+" "+str(ly))
                        cy += slope

                        if abs(ly - int(cy)) >= 1:
                            # print(str(cx)+" "+str(cy)+" "+str(ly)+"2")

                            self.bx.put(int(cx))
                            self.by.put(int(cy))
                            ly = int(cy)
                        cx += d

                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))

                    while(int(cy) != int(self.v[t][1])):
                        d = int((int(self.v[t][1])-cy) /
                                abs((int(self.v[t][1])-cy)))
                        cy += d
                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))
        else:
            for i in range(nV):
                self.by.put(int(self.v[nV-1-i][1]))
                self.bx.put(int(self.v[nV-1-i][0]))
                cx = int(self.v[nV-1-i][0])
                cy = int(self.v[nV-1-i][1])
                t = nV-2-i
                if(t < 0):
                    t = nV-1
                # print(str(i)+" "+str(t))
                if(cx == int(self.v[t][0])):
                    slope = 0
                else:
                    slope = (cy-int(self.v[t][1]))/(cx-int(self.v[t][0]))

                if (abs(slope) > 1):
                    lx = cx
                    while(int(cy) != int(self.v[t][1])):
                        d = - \
                            int(abs(cy-int(self.v[t][1])) /
                                (cy-int(self.v[t][1])))
                        # print(str(cx)+" "+str(cy)+" "+str(lx))

                        cx += d / slope

                        if (abs(int(cx) - lx) >= 1):
                            # print(str(cx)+" "+str(cy)+" "+str(lx)+"2")
                            self.bx.put(int(cx))
                            self.by.put(int(cy))
                            lx = int(cx)
                        cy += d
                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))

                    while(int(cx) != int(self.v[t][0])):
                        d = int((int(self.v[t][0])-cx) /
                                abs((int(self.v[t][0])-cx)))
                        cx += d
                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))
                else:
                    ly = cy
                    while(int(cx) != int(self.v[t][0])):
                        d = - \
                            int(abs(cx-int(self.v[t][0])) /
                                (cx-int(self.v[t][0])))
                        # print(str(cx)+" "+str(cy)+" "+str(ly))

                        cy += slope
                        if abs(ly - int(cy)) >= 1:
                            # print(str(cx)+" "+str(cy)+" "+str(ly)+"2")
                            self.bx.put(int(cx))
                            self.by.put(int(cy))
                            ly = int(cy)
                        cx += d
                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))

                    while(int(cy) != int(self.v[t][1])):
                        d = int((int(self.v[t][1])-cy) /
                                abs((int(self.v[t][1])-cy)))
                        cy += d
                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))
                        
   
     
                
  
    def execute(self,data):
        # print("Execuring")
        qs = self.bx.qsize();
        while (qs > 0):
            qs -= 1
            ry = self.by.get()
            rx = self.bx.get()
            # print("Executing"+ str(rx)+" "+str(ry))
            if(ry<data.nrows and rx<data.ncols and ry>=0 and rx>=0 ):
                data.BURN[ry][rx][1]=2;
            self.bx.put(rx)
            self.by.put(ry)
    def executeFuture(self,data,timee,speedms):
        rng = np.random.RandomState(2025)
        oldburn=data.BURN
        data.reset()
        lx=-1
        ly=-1
        qs= self.bx.qsize();
        ftime=timee
        while(qs>0):
            qs-=1
            rx=self.bx.get();
            ry=self.by.get();
            if(ly!=-1):
                dy=ry-ly;
                dx=rx-lx;
                d=np.sqrt(dy**2+dx**2)
                if(rx>=0 and ry>=0 and rx<data.ncols and ry<data.nrows and lx>=0 and ly>=0 and lx<data.ncols and ly<data.nrows  ):
                    ftime+=(d/(data.getSpeed(ftime,ry,rx,(data.elevation[ry][rx]-data.elevation[ly][lx])/(d*30),0)*2))
                    
            ly=ry
            lx=rx
            if(rx>=0 and ry>=0 and rx<data.ncols and ry<data.nrows):
                if(oldburn[ry][rx][1]>=ftime-10 or oldburn[ry][rx][1]==0):
                    data.FUTURE[ry][rx]=int(ftime)
                    data.BURN[ry][rx][1]=2
            self.bx.put(rx)
            self.by.put(ry)
        rx=int(data.ncols/2)
        ry=int(data.nrows/2)
        pq= Queue(maxsize=0)
        pq.put((rx,ry))
        while(not pq.empty()):
            p=pq.get();
            rx=p[0]
            ry=p[1]
            if(rx>=0 and ry>=0 and rx<data.ncols and ry<data.nrows and (data.BURN[ry][rx][1]==0 )and oldburn[ry][rx][1]!=0  ):
                 data.BURN[ry][rx][1]=oldburn[ry][rx][1]
                 oldburn[ry][rx][1]=0
                #  print(p)
                 pq.put((rx+1,ry))
                 pq.put((rx,ry+1))
                 pq.put((rx,ry-1))
                 pq.put((rx-1,ry))
        file=open("ftoutput.txt",'w')
        for i in range (data.ncols):
            for j in range (data.nrows):
                file.write( str(data.FUTURE[j][i])+" ")
            file.write("\n")
        print(ftime)
        
        
        
 
    def getScore(self,data,time,buffer,speedms,X,color,type):
        X.fill(0)
        score=0;
        lx=-1
        ly=-1
        qs= self.bx.qsize();
        broke=False
        ftime=time
        deaths=0
        if(type=="risky"):
            while(qs>0):
                qs-=1
                rx=self.bx.get();
                ry=self.by.get();
                if(ly!=-1):
                    dy=ry-ly;
                    dx=rx-lx;
                    d=np.sqrt(dy**2+dx**2)
                    if(rx>=0 and ry>=0 and rx<data.ncols and ry<data.nrows and lx>=0 and ly>=0 and lx<data.ncols and ly<data.nrows  ):
                        ftime+=(d/(data.getSpeed(ftime,ry,rx,(data.elevation[ry][rx]-data.elevation[ly][lx])/(d*30),deaths)*2))
                        # print((data.getSpeed(ftime,ry,rx,(data.elevation[ry][rx]-data.elevation[ly][lx])/(d*30))))
                ly=ry
                lx=rx
                bc=0
                if(rx>=0 and ry>=0 and rx<data.ncols and ry<data.nrows):
                    X[ry][rx]=1;
                    if(data.BURN[ry][rx][1]<ftime+buffer and data.BURN[ry][rx][1]>1):
                        #line too late
                        score+=600000
                        if(data.BURN[ry][rx][1]<ftime):
                            broke=True
                            score+=1200000
                            deaths+=1
                            X[ry][rx]=0
                self.bx.put(rx)
                self.by.put(ry)
            # print(ftime)
            # print("ghhfhgfgdgfdfgdgfdgfdfgdgf^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            for i in range(data.ncols):
                inp=False
                lst=False
                store=0
                for j in range(data.nrows):
                    if(X[j][i]==1):
                        
                        lst=True
                    else:
                        if(lst):
                            inp=not inp
                        lst=False
                        
                            
                            
                    
                        
                    if not inp:
                        if(data.BURN[j][i][1]>1):
                            if(data.BURN[j][i][1]<time):
                                score+=70000
                            elif(data.BURN[j][i][1]<ftime):
                                if broke:
                                    score+=100000
                                else:
                                    score+=35000+35000*(ftime-data.BURN[j][i][1])/(ftime-time)
                    else:
                        data.COLORS[j][i]=1;
                    
                        if(data.BURN[j][i][1]>1):
                            if(data.BURN[j][i][1]<time):
                                
                                store+=1
                            elif(data.BURN[j][i][1]<ftime):
                                
                                    store+=1+1*(ftime-data.BURN[j][i][1])/(ftime-time)
                            else: 
                                score+=800
                        else:
                            score+=1000
                if inp:
                    score+=np.absolute(store)*10
                else:
                    score+=store
        elif (type == "fast"):
            while(qs>0):
                qs-=1
                rx=self.bx.get();
                ry=self.by.get();
                if(ly!=-1):
                    dy=ry-ly;
                    dx=rx-lx;
                    d=np.sqrt(dy**2+dx**2)
                    if(rx>=0 and ry>=0 and rx<data.ncols and ry<data.nrows and lx>=0 and ly>=0 and lx<data.ncols and ly<data.nrows  ):
                        ftime+=(d/(data.getSpeed(ftime,ry,rx,(data.elevation[ry][rx]-data.elevation[ly][lx])/(d*30),deaths)*2))
                        # print((data.getSpeed(ftime,ry,rx,(data.elevation[ry][rx]-data.elevation[ly][lx])/(d*30))))
                ly=ry
                lx=rx
                bc=0
                if(rx>=0 and ry>=0 and rx<data.ncols and ry<data.nrows):
                    X[ry][rx]=1;
                    if(data.BURN[ry][rx][1]<ftime+buffer and data.BURN[ry][rx][1]>1):
                        #line too late
                        score+=12000
                        if(data.BURN[ry][rx][1]<ftime):
                            broke=True
                            score+=12000
                            deaths+=1
                            X[ry][rx]=0
                self.bx.put(rx)
                self.by.put(ry)
            # print(ftime)
            # print("ghhfhgfgdgfdfgdgfdgfdfgdgf^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            for i in range(data.ncols):
                inp=False
                lst=False
                store=0
                for j in range(data.nrows):
                    if(X[j][i]==1):
                        
                        lst=True
                    else:
                        if(lst):
                            inp=not inp
                        lst=False
                        
                            
                            
                    
                        
                    if not inp:
                        if(data.BURN[j][i][1]>1):
                            if(data.BURN[j][i][1]<time):
                                score+=600
                            elif(data.BURN[j][i][1]<ftime):
                                if broke:
                                    score+=1200
                                else:
                                    score+=600*(ftime-data.BURN[j][i][1])/(ftime-time)
                    else:
                        data.COLORS[j][i]=1;
                    
                        if(data.BURN[j][i][1]>1):
                            if(data.BURN[j][i][1]<time):
                                
                                store-=500
                            elif(data.BURN[j][i][1]<ftime):
                                
                                    store-=500*(ftime-data.BURN[j][i][1])/(ftime-time)
                            else: 
                                score+=8
                        else:
                            score+=10
                if inp:
                    score+=np.absolute(store)*10
                else:
                    score+=store
        return score
       
        
    
    
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.y2 = y2
        self.x2 = x2

    def intersects(self, other):
        return ((self.x1 <= other.x1 and self.x2 >= other.x1 or other.x1 <= self.x1 and other.x2 >= self.x1) and (
                    self.y1 <= other.y1 and self.y2 >= other.y1 or other.y1 <= self.y1 and other.y2 >= self.y1))


def dir(bp, p1, p2):
    det = (p1[1] - bp[1]) * (p2[0] - p1[0]) - (p1[0] - bp[0]) * (p2[1] - p1[1])
    if det == 0:
        return 0
    elif det > 0:
        return 1;
    else:
        return 2;


def eulerdist2(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


class Genome:
    
    def __init__(self,points,rot=-1):
        self.origin=[0,0]
        avgX=0
        avgY=0
        for point in points:
            avgX+=point[0]
            avgY+=point[1]
        avgX/=len(points)
        avgY/=len(points)
        self.origin[0]=avgX;
        self.origin[1]=avgY
        vert=sorted(points,key=self.clockwise_sort)
        self.score=0
        if rot ==-1:
            rot=np.random.randint(0,len(vert))
        self.rot=rot
        vert=vert[rot:]+vert[:rot];
        self.v=vert;
        # vert=self.convexHull(points)
        # try:
        # print (points)
        # # tri=Delaunay(points)
        # # print(tri)
        # aphshp=alphashape.alphashape(points,2.0)
        # vert=aphshp
        # # vert=vert.coords
        # # vert=points
        # # vert=vert[0]
        # # for geom in vert:
        # #     print(geom)
        # print(vert)
        # self.v=vert
        # self.score=0
        # except:
        #     self.score=999999999
        #     vert=points
        #     self.v=vert
        
        self.lines=[FireLine(vert,len(vert))]       
  
       
    def clockwise_sort(self,p):
        vec=[0,1]
        v=[p[0]-self.origin[0],p[1]-self.origin[1]]
        length=np.hypot(v[0],v[1])
        if length==0:
            return 0,-np.pi
        normalized=[v[0]/length,v[1]/length]
        dotProduct=normalized[0]*vec[0]+normalized[1]*vec[1]
        diffProduct=vec[1]*normalized[0]-vec[0]*normalized[1]
        ang=np.arctan2(diffProduct,dotProduct)
        if ang<0:
            return 2*np.pi+ang,length
        return ang,length

       
    def execute(self,data):
        # print("exuriutingngjdsh")
        for line in self.lines:
            # print("Here")
            line.execute(data)
    def executeFuture(self,data,time,speed):
        # print("exuriutingngjdsh")
        for line in self.lines:
            # print("Here")
            line.executeFuture(data,time,speed)

    def floodFill(self, data, X, simtime):

        q = Queue(0)
        q.put((rx, ry))

        score = 0
        while (not q.empty()):
            p = q.get()
            rx = p[0]
            ry = p[1]

            if not (not (rx >= 0 and ry >= 0 and ry < data.nrows and rx < data.ncols) or X[ry][rx] == 0):

                if (data.BURN[ry][rx] > 0 and data.BURN[ry][rx] <= simtime):
                    score += 1000

    def floodFill(self,data,X,rx,ry,simtime):
        
        q=Queue(0)
        q.put((rx,ry))
     
        score=0
        while(not q.empty()):
            p=q.get()
            rx=p[0]
            ry=p[1]
            
            if not(not(rx  >= 0 and ry  >= 0 and ry< data.nrows and rx  < data.ncols) or X[ry][rx]!=0):
                
                if(data.BURN[ry][rx][1]>0 and data.BURN[ry][rx][1]<=simtime):
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
        return score
                
    def getFitness(self,data,buffer,time,speedms,color,X,type):
        score=0;
        
            
        for l in self.lines:
            
            # print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF1")
            score+=l.getScore(data,buffer,time,speedms,X,color,type)
            
            # print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF2")
            #fix flood fill here
        # for i in range(data.ncols):
        #     for j in range(data.nrows):
        #         score+=self.floodFill(data,X,i,j,time)
        return self.score+score
    

