import threading
import time
import numpy as np

class Fire:
    def __init__(self,x,y,BURN,tick,p):
        self.x=x
        self.y=y
        rx=int(self.x/p)
        ry=int(self.y/p)
        if(BURN[rx][ry][2]==0):

            # rothermel stuff here
            
            self.direction=(np.random.random())*2*3.14#TODO change this  # Direction in radians
            # self.coneAngle=0.08 #TODO change this # Angle of cone in direction  image the direction is the center of an arc and fire spreads in through the cone at that rate
            self.speed=np.random.randint(60)+10  #TODO change this # Speed in m/min 
            self.nextT=[]
            BURN[ry][rx][0]=self.speed
            BURN[ry][rx][1]=self.direction
            BURN[ry][rx][2]=tick
            t=threading.Thread(target=self.preCompute, args=(x,y,p,tick,BURN))
            t.start()
    
    def preCompute(self,x,y,p,tick,BURN):
        # print(str(tick) +" "+str(x)+" "+str(y)+" \n")
        print(" ("+str(x)+","+str(y)+") \n")
        dx=self.speed*np.cos(self.direction)
        dy=self.speed*np.sin(self.direction)
        tx=p*np.cos(self.direction)
        ty=p*np.sin(self.direction)  
        
        if(dx**2+dy**2>p**2):
      
            
            x+=tx
            y+=ty
            if(x>=0 and y>=0 and x<48000 and y<48000):
                Fire(x,y,BURN,tick+p/np.sqrt(dx**2+dy**2),p)
        else:
            x+=dx
            y+=dy
            if(x>=0 and y>=0 and x<48000 and y<48000):
                Fire(x,y,BURN,tick+1,p)
   
   
        
        
        