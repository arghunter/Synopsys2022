

from data import *
from fire import *
import threading
import time
from GA import *

# print("AAAAAAAAAAAAAAAAAAAAAAA")
# print(a)

data=Data()

fire=Fire(data.ncols/2*data.p,data.nrows/2*data.p,data,1,data.ncols/2*data.p+data.p,data.nrows/2*data.p+data.p)


# fire=Fire(100,100,data,1,data.nrows/2*data.p+data.p,data.ncols/2*data.p+data.p)
# fire=Fire(data.ncols/2*data.p,165*data.p,data,1,data.ncols/2*data.p+data.p,data.nrows/2*data.p+data.p)


while(threading.activeCount()>1):
    print(threading.activeCount())
    time.sleep(1)

# solve(data,3840,10)

file=open("routput.txt",'w')
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