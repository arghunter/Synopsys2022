import threading
import time
import numpy as np
from data import *
class Fire:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        # rothermel stuff here
        
        self.direction= 0#TODO change this  # Direction in radians
        # self.coneAngle=0.08 #TODO change this # Angle of cone in direction  image the direction is the center of an arc and fire spreads in through the cone at that rate
        self.speed=1  #TODO change this # Speed in m/s 
        self.nextT=[]
        t=threading.Thread(target=self.preCompute, args=(self))
        t.start()
    def preCompute(self):
        dx=self.speed*np.cos(self.direction)
        dy=self.speed*np.sin(self.direction)
        tx=p*np.cos(self.direction)
        ty=p*np.sin(self.direction)  
        while(dx**2+dy**2>p**2):
      
            dx-=tx
            dy-=ty
            x+=tx
            y+=ty
            self.nextT.append(Fire(x,y))
        x+=dx
        y+=dy
        self.nextT.append(Fire(x,y))
        compute+=1
    #NOTE: ALWAYS CALL THIS AS A THREAD UPON THE IGNITION SOURCE
    def tick(self,BURN,tick,interval):
        t=threading.Thread(target=self.__tick,args=(self,BURN,tick,interval))
        
    def __tick(self,BURN,tick,interval):
        rx=self.x/p
        ry=self.y/p
        if(BURN[rx][ry]==0):
            BURN[ry][rx][0]=self.speed
            BURN[ry][rx][1]=self.direction
            BURN[ry][rx][2]=tick
            time.sleep(interval)
            for fire in self.nextT:
                fire.tick(BURN,tick+1,interval)
        
        
        