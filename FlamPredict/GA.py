import time
from tkinter.tix import Tree
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import animation
from matplotlib import colors
from queue import Queue
import threading
from scipy.spatial import ConvexHull, convex_hull_plot_2d

# import files


# altitude init
# from altitudeGen import *

# genome init
from genome import *
neighborhood = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                (0, 1), (1, -1), (1, 0), (1, 1)]
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
    popCount=120
    genCount=60
    elite=int(popCount*0.1)
    bRes=30
    opRounds=12
    pop=np.empty(popCount,Genome)
    mins=2000000000
    ming=None
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
    for i in range (data.ncols):
        for j in range (data.nrows):
            if(data.BURN[j][i][1]>1 and data.BURN[j][i][1]<buffer+safetyTime):
                seti.add((i,j));
                
    lst=list(seti)
    hull=ConvexHull(lst)
    verts=hull.points[hull.vertices];
    
    
    bRes=len(verts)
    
                
    
    # gnme=Genome(points)
    # print(gnme.getFitness(data,buffer,safetyTime,3,1,X))
    # gnme.execute(data)
    for i in range(popCount):
        points=np.zeros((bRes,2))
        w=np.zeros(bRes)
        left=1
        td=0
        
        for t in range(bRes):
            px= np.random.randint(-32,32);
            py= np.random.randint(-32,32);
            points[t][0]=px+verts[t][0];
            points[t][1]=py+verts[t][1];
            if t>0:
                td+=np.sqrt((points[t][0]-points[t-1][0])**2+(points[t][1]-points[t-1][1])**2)
        td+=np.sqrt((points[bRes-1][0]-points[0][0])**2+(points[bRes-1][1]-points[0][1])**2)    
        for t in range(1,bRes):
    
            
            w[t-1]=np.sqrt((points[t][0]-points[t-1][0])**2+(points[t][1]-points[t-1][1])**2)/td
        w[bRes-1]=np.sqrt((points[bRes-1][0]-points[0][0])**2+(points[bRes-1][1]-points[0][1])**2)/td
        
        
        # ty:
        #     hull=ConvexHull(points)
        #     points=hull.points[hull.vertices]
        # except:
        #     pass
        pop[i]=Genome(points,w)
    scores=np.zeros(popCount)
    for i in range(genCount):
        X=np.zeros(data.COLORS.shape)
        print(i/genCount)
        for j in range(popCount):
            print(j)
            scores[j]=pop[j].getFitness(data,buffer,safetyTime,30,j,X)#add speed
        ind= np.argsort(scores)
        scores=scores[ind]
        pop=pop[ind]
        if scores[0]<mins:
            mins=scores[0]
            ming=pop[0]
        print(ming.w)
        # par1=ming
        par2=np.random.randint(0,elite)
        p1=ming.v
        p2=pop[par2].v
        split=np.random.randint(1,min(len(p1)-1,len(p2)-1))
        p3=p1[0:split]+p2[split:len(p2)]
        
        if(np.random.random()<0.8):
            pos=np.random.randint(0,len(p3))
            point=p3[pos];
            dx=np.random.randint(-8,8);
            dy=np.random.randint(-8,8);
            if(point[1]+dx>=0 and point[0]+dy>=0 and point[0]+dy<data.nrows and point[1]+dx<data.ncols ):
                p3[pos]=(dy+point[0],dx+point[1])
            
        wV=np.random.random()
        
        if wV<0.5:
            
            w=ming.w
        else:
            
            w=pop[par2].w
        if np.random.random()<0.4:
            
            
            w=ming.w
            w1=np.random.randint(0,bRes);
            w2=np.random.randint(0,bRes);
            valw=np.random.uniform(0,w[w1])
            w[w2]+=valw
            w[w1]-=valw
            
        pop[0]=Genome(p3,w)
        for j in range(1,popCount):
            par1=np.random.randint(0,elite)
            par2=np.random.randint(0,elite)
            p1=pop[par1].v
            p2=pop[par2].v
            if(np.random.random()<0.2):
                par1=np.random.randint(elite,popCount)
                p1=pop[par1].v
                
            if(np.random.random()<0.2):
                par2=np.random.randint(elite,popCount)
                p2=pop[par2].v
            
            split=np.random.randint(1,min(len(p1)-1,len(p2)-1))
            
            p3=p1[0:split]+p2[split:len(p2)]
            if(np.random.random()<0.8):
                pos=np.random.randint(0,len(p3))
                point=p3[pos];
                dx=np.random.randint(-8,8);
                dy=np.random.randint(-8,8);
                if(point[1]+dx>=0 and point[0]+dy>=0 and point[0]+dy<data.nrows and point[1]+dx<data.ncols ):
                    p3[pos]=(dy+point[0],dx+point[1])
            
            wV=np.random.random()
            
            if wV<0.5:
                
                w=pop[par1].w
            else :
                
                w=pop[par2].w
            wV=np.random.random()
            if wV<0.4:
                rot=int((pop[par1].rot+pop[par2].rot)/2)
                w=ming.w
                w1=np.random.randint(0,bRes);
                w2=np.random.randint(0,bRes);
                valw=np.random.uniform(0,w[w1])
                w[w2]+=valw
                w[w1]-=valw
           
            pop[j]=Genome(p3,w)
        print(scores)
    
    scores=np.zeros(popCount)
    # for i in range(genCount):
    X=np.zeros(data.COLORS.shape)
    # print(i/genCount)
    for j in range(popCount):
        print(j)
        scores[j]=pop[j].getFitness(data,buffer,safetyTime,30,j,X)#add speed
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
    so=Genome(pop[0].v,pop[0].w);
    fit=so.getFitness(data,buffer,safetyTime,30,j,X)
   
    
    
 
    vert=pop[0].v

    minfit=fit;
       
    # fitarray=np.zeros((len(vert),8))
    t=0
    tvv=vert.copy()
    while t<opRounds: 
        print(t)
        print(fit)
        
        for i in range(0,len(vert)):
            tminfit=fit
            dir=-1
            for j in range(len(neighborhood)):
                tv=tvv.copy()
                # print(tv[i][0])
                tv[i]=(tv[i][0]+neighborhood[j][0],tv[i][1]+neighborhood[j][1])
                
                tempgnme=Genome(tv,pop[0].w)
                tempfit=tempgnme.getFitness(data,buffer,safetyTime,30,1,X)
                if tempfit<tminfit:
                    tminfit=tempfit
                    dir=j     
            if dir!=-1:
                tvv[i]=(tv[i][0]+neighborhood[dir][0],tv[i][1]+neighborhood[dir][1])
                fit=tminfit
        
        t+=1
       
    

        
    
            
            
            

    
            
    sol=Genome(tvv,pop[0].w);    
            
                    
            
    sol.executeFuture(data,buffer,2);
    print(str(sol.v))
               
        
    # print(rects)    


  

    # print(rects)





# sol = Genome(4)


