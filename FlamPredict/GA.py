import time
from tkinter.tix import Tree
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import animation
from matplotlib import colors
from queue import Queue
import threading

# import files


# altitude init
# from altitudeGen import *

# genome init
from genome import *

def solve(data,buffer,safetyTime):
    # X=np.zeros(data.COLORS.shape)
    # points= np.array([[15,120],[15,290],[200,290],[100,130],[200,150],[200,120]])
# hull=ConvexHull(points);

# points = rng.random((30, 2))
    # hull=ConvexHull(points)
    # print(hull.points[hull.vertices])
    # g1=Genome(hull.points[hull.vertices])
    # print(g1.getFitness(data,buffer,safetyTime,1.2,1,X))
    # g1.execute(data);
    
    # pass
    popCount=100
    genCount=50
    elite=int(popCount*0.1)
    bRes=16
    pop=np.empty(popCount,Genome)
    seti=set()
    # for i in range (data.ncols):
    #     for j in range (data.nrows):
    #         if(data.BURN[j][i][1]!=0 and data.COLORS[j][i]==0):
    #             floodFill(data,i,j,4,safetyTime+buffer,seti)
    # lst=list(seti)
    # points=convexHull(lst)
    # for i in range(len(lst)):
    #     data.BURN[lst[i][1]][lst[i][0]][1]=i
        
    
    # for i in range(popCount):
        
    # points=[(10,10),(30,20),(80,110),(90,60)]
    # X=np.zeros(data.COLORS.shape)
    # # for t in range(bRes):
    # #     px= np.random.randint(10,data.nrows-10);
    # #     py= np.random.randint(10,data.ncols-10);
    # #     points.append((px,py))

    # gnme=Genome(points)
    # print(gnme.getFitness(data,buffer,safetyTime,3,1,X))
    # gnme.execute(data)
    for i in range(popCount):
        points=np.zeros((bRes,2))
        for t in range(bRes):
            px= np.random.randint(10,data.nrows-10);
            py= np.random.randint(10,data.ncols-10);
            points[t][0]=px;
            points[t][1]=py;
        try:
            hull=ConvexHull(points)
            points=hull.points[hull.vertices]
        except:
            pass
        pop[i]=Genome(points)
    scores=np.zeros(popCount)
    for i in range(genCount):
        X=np.zeros(data.COLORS.shape)
        print(i/genCount)
        for j in range(popCount):
            print(j)
            scores[j]=pop[j].getFitness(data,buffer,safetyTime,5,j,X)#add speed
        ind= np.argsort(scores)
        scores=scores[ind]
        pop=pop[ind]
        # print(scores)
        for j in range(popCount):
            p1=pop[np.random.randint(0,elite)].v
            p2=pop[np.random.randint(0,elite)].v
            if(np.random.random()<0.2):
                p1=pop[np.random.randint(elite,popCount)].v
                
            if(np.random.random()<0.2):
                p2=pop[np.random.randint(elite,popCount)].v
            
            split=np.random.randint(1,min(len(p1)-1,len(p2)-1))
            
            p3=p1[0:split]+p2[split:len(p2)]
            if(np.random.random()<0.1):
                pos=np.random.randint(0,len(p3))
                point=p3[pos];
                dx=np.random.randint(1,64)-32;
                dy=np.random.randint(1,64)-32;
                if(point[1]+dx>=0 and point[0]+dy>=0 and point[0]+dy<data.nrows and point[1]+dx<data.ncols ):
                    p3[pos]=(dy+point[0],dx+point[1])
            pop[j]=Genome(p3)
        print(scores)
    
    scores=np.zeros(popCount)
    # for i in range(genCount):
    X=np.zeros(data.COLORS.shape)
    # print(i/genCount)
    for j in range(popCount):
        print(j)
        scores[j]=pop[j].getFitness(data,buffer,safetyTime,5,j,X)#add speed
    ind= np.argsort(scores)
    scores=scores[ind]
    pop=pop[ind]
            
    # for 
     # The squared distance for 2 spots to be unique clusters
   
    # rect=[2000000000,2000000000,-1,-1]

    # sol=Genome(rects)
    # print("qiwoyhe had ")
    # # t=pop[0].getFitness(data,buffer,safetyTime,3,genCount+1,)
    # # print(t)
    # # pop[0].execute(data)
    so=Genome(pop[0].v);
    so.getFitness(data,buffer,safetyTime,5,j,X)
    sol=Genome(pop[0].v);
    sol.execute(data);
               
        
    # print(rects)    

def floodFill(data,rx,ry,color,simtime,seti):
    q=Queue(0)
    q.put((rx,ry))
    
    while(not q.empty()):
        p=q.get()
        rx=p[0]
        ry=p[1]
        
        if not(not(rx  >= 0 and ry  >= 0 and ry< data.nrows and rx  < data.ncols) or data.COLORS[ry][rx]!=0 or data.BURN[ry,rx,1]==0 or data.BURN[ry][rx][1]>simtime):
            seti.add((rx,ry))
        
            data.COLORS[ry][rx]=color
            q.put((rx+1,ry))
            q.put((rx-1,ry))
            q.put((rx,ry+1))
            q.put((rx,ry+1))
            q.put((rx+1,ry+1))
            q.put((rx+1,ry-1))
            q.put((rx-1,ry-1))
            q.put((rx-1,ry+1))
  

    # print(rects)


bp = (0, 0)


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


def cmp(a, b):
    # return a[0]<b[0];
    dr = dir(bp, a, b)
    if dr == 0:
        if (eulerdist2(bp, b) >= eulerdist2(bp, a)):
            return -1;
        else:
            return 1;
    else:
        if dr == 2:
            return -1
        else:
            return 1


def convexHull(points):
    minv = points[0][1]
    min = 0
    for i in range(1, len(points)):
        if (points[i][1] < minv or points[i][1] == minv and points[i][0] < points[min][0]):
            minv = points[i][1]
            min = i
    points[0], points[min] = points[min], points[0]
    bp = points[0];
    nl = 1
    points = sorted(points, key=cmp_to_key(cmp))
    for i in range(1, len(points)):
        while ((i < len(points) - 1)) and (dir(bp, points[i], points[1]) == 0):
            i += 1
        points[nl] = points[i]
        nl += 1
    if nl < 3:
        return
    vert = [points[0], points[1], points[2]]
    for i in range(3, nl):
        while (len(vert) > 1) and (dir(vert[-2], vert[-1], points[i]) != 2):
            vert.pop()
        vert.append(points[i])
    return vert


def floodFill(data, rx, ry, color, simtime, seti):
    q = Queue(0)
    q.put((rx, ry))
    x1 = rx
    x2 = rx
    y1 = ry
    y2 = ry
    while (not q.empty()):
        p = q.get()
        rx = p[0]
        ry = p[1]

        if not (not (rx >= 0 and ry >= 0 and ry < data.nrows and rx < data.ncols) or data.COLORS[ry][rx] != 0 or
                data.BURN[ry, rx, 1] == 0 or data.BURN[ry][rx][1] > simtime):
            seti.add((ry, rx))
            if (rx < x1):
                x1 = rx
            elif (rx > x2):
                x2 = rx
            if (ry < y1):
                y1 = ry
            elif (ry > y2):
                y2 = ry

            print(str(data.COLORS[ry][rx]) + " " + str(ry) + " " + str(rx) + " " + str(x1) + " " + str(y1) + " " + str(
                x2) + " " + str(y2))
            data.COLORS[ry][rx] = color
            q.put((rx + 1, ry))
            q.put((rx - 1, ry))
            q.put((rx, ry + 1))
            q.put((rx, ry + 1))
            q.put((rx + 1, ry + 1))
            q.put((rx + 1, ry - 1))
            q.put((rx - 1, ry - 1))
            q.put((rx - 1, ry + 1))
    print(str((x1, y1, x2, y2)))
    return (x1, y1, x2, y2)

# sol = Genome(4)


