

from data import *
from fire import *
import threading
import time
from GA import *

# print("AAAAAAAAAAAAAAAAAAAAAAA")
# print(a)
rng = np.random.RandomState(2025)
data=Data()
fire=Fire(data.ncols/2*data.p,data.nrows/2*data.p,data,1,data.ncols/2*data.p+data.p,data.nrows/2*data.p+data.p,rng)

gnmes=[]
scores=[]

# fire=Fire(100,100,data,1,data.nrows/2*data.p+data.p,data.ncols/2*data.p+data.p)
# fire=Fire(data.ncols/2*data.p,165*data.p,data,1,data.ncols/2*data.p+data.p,data.nrows/2*data.p+data.p)


while(threading.activeCount()>1):
    print(threading.activeCount())
    time.sleep(1)

# solve(data,3840,60).executeFuture(data,3840,60)
# t=threading.Thread(target=solve,args=(data,3840,60,gnmes))
# t.start()
# t=threading.Thread(target=solve,args=(data,3840,60,gnmes))
# t.start()
# solve(data,3840,60,gnmes)
# solve(data,3840,60,gnmes)
timeBegin=3300
buffer=90
ep=[]
t=threading.Thread(target=solve,args=(data,timeBegin,buffer,gnmes,ep,0,"hybrid"))
t.start()
# t=threading.Thread(target=solve,args=(data,timeBegin,buffer+30,gnmes,ep,1))
# t.start()
# t=threading.Thread(target=solve,args=(data,timeBegin,buffer-30,gnmes,ep,2))
# t.start()
while(threading.activeCount()>1):
    print(threading.activeCount())
    time.sleep(10)
X=np.zeros(data.COLORS.shape)
for gnme in gnmes:
    scores.append(gnme.getFitness(data,timeBegin,buffer,30,0,X,"risky"))
min=100000000000000000000000
mini=0
for i in range(len(scores)):
    if(scores[i]<min):
        min=scores[i]
        mini=i;
gnmes[mini].executeFuture(data,timeBegin,buffer)
file=open("routput25hybrid.txt",'w')
for i in range (data.ncols):
    for j in range (data.nrows):
        file.write( str(data.BURN[j][i][1])+" ")
    file.write("\n")
# print(B)
file=open("coutput.txt",'w')
for i in range (data.ncols):
    for j in range (data.nrows):
        file.write( str(data.COLORS[j][i])+" ")
    file.write("\n")
print(min)    