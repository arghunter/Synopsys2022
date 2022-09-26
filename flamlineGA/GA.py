import time
from tkinter.tix import Tree
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import animation
from matplotlib import colors
from queue import Queue
import threading
from scorer import Scorer

# import files
from userInfo import *


# altitude init
# from altitudeGen import *

# genome init
from genome import *

popCount = 100
genCount=100
elite=8
# sol = Genome(4)


def getSol(X, A):
    print("Solvin")
    population = np.empty(popCount, Genome)
    scores = np.zeros(popCount)
    count=np.zeros(1)
    # min = 21347000000
    # mini = 0
    # min2 = 21347000000
    # minii = 0
    for i in range(popCount):
        population[i] = Genome(12)
        print(i)
        t= (threading.Thread(target=test_genome, args=(population[i],X,A,i,scores,count)))
        
        t.start()
    while count[0]!=-popCount:
        time.sleep(1)
        print(count[0])

    ind= np.argsort(scores)
    scores=scores[ind]
    population=population[ind]
    for i in range(genCount):
        print(i/genCount)
        randCount=int(np.random.random()*25)
        parents=np.empty(elite+randCount,Genome)
        for i in range(elite):
            parents[i]=population[i]
        for i in range(elite,elite+randCount):
            parents[i]=population[np.random.randint(popCount)]
        replaced=0
        while replaced<popCount:
            p1=np.random.randint(0,elite+randCount)
            p2=np.random.randint(0,elite+randCount)
            split=np.random.randint(12)
            population[replaced]=Genome(12,parents[p1],parents[p2],split)
            replaced+=1
            if(replaced<popCount):
                population[replaced]=Genome(12,parents[p2],parents[p2],split)
        count[0]=0
        for i in range(popCount):
            t= (threading.Thread(target=test_genome, args=(population[i],X,A,i,scores,count)))
            t.start()
        while count[0]!=-popCount:
            time.sleep(1)
            print(count[0])
            print("Computing")
        ind= np.argsort(scores)
        scores=scores[ind]
        population=population[ind]
        
        
            
        
    print(scores)
    # sol = population[mini]
    # return population[mini]
    return population[0]
    # for i in range(popCount):
    #     print(population[i].nV)

def test_genome(gnme,X,A,i,scores,count):
    print("Testing: "+str(i))
    scorer = Scorer(gnme, X, A)
    scores[i] = scorer.score()
    count[0]-=1;
    
    
# population in generation
# if len(populationBig) <= intpopulationSize:
#     populationBig.append(1)
#     print("POPULATION: ", len(populationBig), "OUT OF", intpopulationSize)
