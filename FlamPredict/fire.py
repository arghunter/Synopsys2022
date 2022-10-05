import threading
import time
import numpy as np

from rothermelModel import *

class Fire:
    def __init__(self, x, y, BURN, tick, p, lastX, lastY, A):
        self.x = x
        self.y = y
        rx = int(self.x / p)
        ry = int(self.y / p)
        rlastX = int(lastX / p)
        rlastY = int(lastY / p)
        if (BURN[rx][ry][2] == 0):
            # rothermel stuff here

            # slope from current cell to spread to cell
            # print(A)
            # altitude of spread to cell
            z2 = (A[ry][rx])
            # altitude of current cell
            z1 = (A[rlastY][rlastX])
            # delta = z diff
            dz = float(z2-z1)
            rdz = float(round(dz, 10))
            # if rx ry changes ingnite the nearest 3 squaesi
            
               
           
            x1 = (lastX)  # x1
            dx = (x - lastX)
            sdx = ((dx) ** 2)
        
            dy = (y - lastY)
            sdy = ((dy) ** 2)
            

            # 2d distance = dxy
            dxy = np.sqrt((sdx + sdy))
            rdxy = float(round(dxy, 10))

            # 3d slope between (x1,y1,z1), (x2,y2,z2)
            Phi = (float(rdz / (rdxy+0.000001)) * 100)
            #print("slope %", Phi)

            # wind velocity at midflame height (ft/min)
            U = 1 # wind 1
            if(rx!=rlastX or ry != rlastY):
                if(not(rx<=0 or ry<=0 or rx>5999 or ry>5999)):
                    Fire(x-(rx-rlastX)*p,y,BURN,tick+p/dxy,p,(x+lastX)/2,(lastY+y)/2,A)
                    Fire(x,y-(ry-rlastY)*p,BURN,tick+p/dxy,p,(x+lastX)/2,(y+lastY)/2,A)
            # m/s to ft/min 196.85


            directionRad = np.arctan(dy/(dx+0.00001))
            if dx < 0:
                directionRad += np.pi

            self.direction = directionRad  # TODO change this  # Direction in radians
            # self.coneAngle=0.08 #TODO change this # Angle of cone in direction  image the direction is the center of an arc and fire spreads in through the cone at that rate
            self.speed = rothermelRate(Phi, U)  # TODO change this # Speed in m/min
            self.nextT = []
            BURN[ry][rx][0] = self.speed
            BURN[ry][rx][1] = self.direction
            BURN[ry][rx][2] = tick
            t = threading.Thread(target=self.preCompute, args=(x, y, p, tick, BURN, A))
            t.start()

    def preCompute(self, x, y, p, tick, BURN, A):
        # print(str(tick) +" "+str(x)+" "+str(y)+" \n")
        # print(" (" + str(x) + "," + str(y) + ") \n")
        f =open("output.txt", "a")
        f.write(" (" + str(x) + "," + str(y) + ") \n")
        f.close()
        dx = self.speed * np.cos(self.direction)
        dy = self.speed * np.sin(self.direction)
        tx = p * np.cos(self.direction)
        ty = p * np.sin(self.direction)

        if (dx ** 2 + dy ** 2 > p ** 2):

            x += tx
            y += ty
            if (x >= 0 and y >= 0 and x < 48000 and y < 48000):
                Fire(x, y, BURN, tick + p / np.sqrt(dx ** 2 + dy ** 2), p, self.x, self.y, A)
        else:
            x += dx
            y += dy
            if (x >= 0 and y >= 0 and x < 48000 and y < 48000):
                Fire(x, y, BURN, tick + 1, p, self.x, self.y, A)




