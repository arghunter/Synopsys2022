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
    rects=[]
    cdist=(180*data.p)**2 # The squared distance for 2 spots to be unique clusters
    qs=data.spotQ.qsize()
    # rect=[2000000000,2000000000,-1,-1]
    for y in range(data.COLORS.shape[0]):
        for x in range(data.COLORS.shape[1]):
        # print(data.spotQ.qsize())
            # data.BURN[int(y/data.p)][int(x/data.p)]=1000
            if( data.COLORS[int(y)][int(x)]==0):
                
                
                rect=floodFill(data,int(x),int(y),len(rects)+100,buffer+safetyTime)
                # print(rect)
                
                if(rect[0]!=rect[2] and rect[1]!=rect[3]  ):
                    # pass
                    rects.append(rect)
                    data.BURN[rect[1]][rect[0]][1]=1
                    data.BURN[rect[3]][rect[0]][1]=1
                    data.BURN[rect[3]][rect[2]][1]=1
                    data.BURN[rect[1]][rect[2]][1]=1
    for rect in rects:
        for j in range(rect[1],rect[3]):
            data.COLORS[j][rect[0]]=1
            data.COLORS[j][rect[2]]=1
               
        
    print(rects)    

def floodFill(data,rx,ry,color,simtime):
    q=Queue(0)
    q.put((rx,ry))
    x1=rx
    x2=rx
    y1=ry
    y2=ry
    while(not q.empty()):
        p=q.get()
        rx=p[0]
        ry=p[1]
        
        if not(not(rx  >= 0 and ry  >= 0 and ry< data.nrows and rx  < data.ncols) or data.COLORS[ry][rx]!=0 or data.BURN[ry,rx,1]==0 or data.BURN[ry][rx][1]>simtime):
             
            if(rx<x1):
                x1=rx
            elif(rx>x2):
                x2=rx
            if(ry<y1):
                y1=ry
            elif(ry>y2):
                y2=ry
            
            print(str(data.COLORS[ry][rx])+" "+ str(ry)+" "+str(rx)+" "+str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2))
            data.COLORS[ry][rx]=color
            q.put((rx+1,ry))
            q.put((rx-1,ry))
            q.put((rx,ry+1))
            q.put((rx,ry+1))
            q.put((rx+1,ry+1))
            q.put((rx+1,ry-1))
            q.put((rx-1,ry-1))
            q.put((rx-1,ry+1))
    print(str((x1,y1,x2,y2)))        
    return (x1,y1,x2,y2)

      

# sol = Genome(4)



