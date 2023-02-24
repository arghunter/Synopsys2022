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
def solve(data,buffer,safetyTime,gnmes,ep,id,type):
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
    popCount=80
    genCount=80
    elite=int(popCount*0.1)
    bRes=30
    opRounds=10
    pop=np.empty(popCount,Genome)
    ep.append(pop)
    seti=set()
    ctype=type
    if type=="hybrid":
        ctype="fast"
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
    file=open("shoutput"+str(id)+".txt",'w');
                
    
    # gnme=Genome(points)
    # print(gnme.getFitness(data,buffer,safetyTime,3,1,X))
    # gnme.execute(data)
    for i in range(popCount):
        points=np.zeros((bRes,2))
        for t in range(bRes):
            px= np.random.randint(-32,32);
            py= np.random.randint(-32,32);
            points[t][0]=px+verts[t][0];
            points[t][1]=py+verts[t][1];
        # try:
        #     hull=ConvexHull(points)
        #     points=hull.points[hull.vertices]
        # except:
        #     pass
        pop[i]=Genome(points)
    scores=np.zeros(popCount)
    for i in range(genCount):
        X=np.zeros(data.COLORS.shape)
        print(i/genCount)
        if(type=="hybrid"and i/genCount>0.5):
            ctype="risky"
            
        for j in range(popCount):
            print(j)
            scores[j]=pop[j].getFitness(data,buffer,safetyTime,30,j,X,ctype)#add speed
        ind= np.argsort(scores)
        scores=scores[ind]
        pop=pop[ind]
        
        file.write(""+str(scores[0])+"\n")
        # print(scores)
        if(np.random.random()<(genCount+2*np.sqrt(i))/(3*genCount)):
            pos=id+1
            if(pos>=len(ep)):
                pos=0;
            for j in range(int(elite/3)):
                swpp=np.random.randint(0,popCount)
              
                tempg=Genome(ep[pos][swpp].v,ep[pos][swpp].rot)
                ep[pos][swpp]=Genome(pop[swpp].v,pop[swpp].rot)
                pop[swpp]=tempg
            
                
        for j in range(popCount):
            par1=np.random.randint(0,elite)
            par2=np.random.randint(0,elite)
            p1=pop[par1].v
            p2=pop[par2].v
            if(np.random.random()<(genCount+2*np.sqrt(i))/(3*genCount)):
                par1=np.random.randint(elite,popCount)
                p1=pop[par1].v
                
            if(np.random.random()<(genCount+2*np.sqrt(i))/(3*genCount)):
                par2=np.random.randint(elite,popCount)
                p2=pop[par2].v
            
            split=np.random.randint(1,min(len(p1)-1,len(p2)-1))
            
            p3=p1[0:split]+p2[split:len(p2)]
            if(np.random.random()<(genCount+2*np.sqrt(i))/(3*genCount)):
                pos=np.random.randint(0,len(p3))
                point=p3[pos];
                dx=np.random.randint(-8,8);
                dy=np.random.randint(-8,8);
                if(point[1]+dx>=0 and point[0]+dy>=0 and point[0]+dy<data.nrows and point[1]+dx<data.ncols ):
                    p3[pos]=(dy+point[0],dx+point[1])
            
            rotV=np.random.random()
            
            if rotV<0.45:
                rot=pop[par1].rot
            elif rotV>0.55:
                rot=pop[par2].rot
            else:
                rot=int((pop[par1].rot+pop[par2].rot)/2)
            if(np.random.random()<0.1):
                    # try:
                    #     hull=ConvexHull(p3)
                    #     hullvert=hull.points[hull.vertices];
                    #     pop[j]=Genome(hullvert)
                    # except:
                    pop[j]=Genome(p3,rot)
            else:
                pop[j]=Genome(p3,rot)
        print(scores)
    
    scores=np.zeros(popCount)
    # for i in range(genCount):
    X=np.zeros(data.COLORS.shape)
    # print(i/genCount)
    for j in range(popCount):
        print(j)
        scores[j]=pop[j].getFitness(data,buffer,safetyTime,30,j,X,ctype)#add speed
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
    so=Genome(pop[0].v,pop[0].rot);
    fit=so.getFitness(data,buffer,safetyTime,30,j,X,ctype)
   
    
    
 
    vert=pop[0].v
    rot=pop[0].rot
    maxrot=rot
    minfit=fit;
    for i in range(len(pop[0].v)):
        tempgnme=Genome(pop[0].v,i)
        tempfit=tempgnme.getFitness(data,buffer,safetyTime,30,j,X,ctype)
        if tempfit <minfit:
            maxrot=i
            minfit=tempfit
    fit=minfit        
    # fitarray=np.zeros((len(vert),8))
    t=opRounds
    tvv=vert.copy()
    while t>0: 
        print(t)
        print(fit)
        
        for i in range(0,len(vert),2):
            tminfit=fit
            dir=-1
            for j in range(len(neighborhood)):
                tv=tvv.copy()
                print(tv[i][0])
                tv[i]=(tv[i][0]+neighborhood[j][0]*t,tv[i][1]+neighborhood[j][1]*t)
                
                tempgnme=Genome(tv,i)
                tempfit=tempgnme.getFitness(data,buffer,safetyTime,30,1,X,ctype)
                if tempfit<tminfit:
                    tminfit=tempfit
                    dir=j     
            if dir!=-1:
                tvv[i]=(tv[i][0]+neighborhood[dir][0]*t,tv[i][1]+neighborhood[dir][1]*t)
                fit=tminfit
        for i in range(1,len(vert),2):
            tminfit=fit
            dir=-1
            for j in range(len(neighborhood)):
                tv=tvv.copy()
                tv[i]=(tv[i][0]+neighborhood[j][0]*t,tv[i][1]+neighborhood[j][1]*t)
                
                tempgnme=Genome(tv,i)
                tempfit=tempgnme.getFitness(data,buffer,safetyTime,30,1,X,ctype)
                if tempfit<tminfit:
                    tminfit=tempfit
                    dir=j     
            if dir!=-1:
                tvv[i]=(tv[i][0]+neighborhood[dir][0]*t,tv[i][1]+neighborhood[dir][1]*t)
                fit=tminfit
        t-=1
        if not (fit<minfit):
            break;
    

        
    
            
            
            

    
            
    sol=Genome(tvv,maxrot);    
            
                    
    gnmes.append(sol)       
    # sol.executeFuture(data,buffer,2);
    # print(str(sol.v))
               
        
    # print(rects)    


  

    # print(rects)





# sol = Genome(4)


