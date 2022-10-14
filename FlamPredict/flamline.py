

from data import *
from fire import *
import threading
import time
# print("AAAAAAAAAAAAAAAAAAAAAAA")
# print(a)
data=Data()
fire=Fire(data.nrows/2*data.p,data.ncols/2*data.p,data,1,data.nrows/2*data.p+data.p,data.ncols/2*data.p+data.p)
file=open("output.txt",'w')
while(threading.activeCount()>1):
    print(threading.activeCount())
    time.sleep(1)
    
for i in range (data.ncols):
    file.write(str(data.BURN[i]))
# print(B)