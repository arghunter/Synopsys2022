import threading
import time
import numpy as np
from data import *
from rothermelModel import *

# The neightbors of a cells
neighborhood = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                (0, 1), (1, -1), (1, 0), (1, 1))


class Fire:
    def __init__(self, x, y, data, tick, lastX, lastY):
        self.x = x
        self.y = y
        self.lastX = lastX;
        self.lastY = lastY;
        rx = int(self.x / data.p)
        ry = int(self.y / data.p)
        rlastX = int(lastX / data.p)
        rlastY = int(lastY / data.p)
        print("(" + str(rx) + "," + str(ry) + ")")

        # rothermel stuff here

        # slope from current cell to spread to cell
        # print(A)
        # altitude of spread to cell
      
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
  
        # print("slope %", Phi)

        # wind velocity at midflame height (ft/min)
        U = 1  # wind 1
        # if(rx!=rlastX or ry != rlastY):
        #     if(not(rx<=0 or ry<=0 or rx>5999 or ry>5999)):
        #         Fire(x-(rx-rlastX)*p,y,BURN,tick+p/dxy,p,(x+lastX)/2,(lastY+y)/2,A)
        #         Fire(x,y-(ry-rlastY)*p,BURN,tick+p/dxy,p,(x+lastX)/2,(y+lastY)/2,A)
        # m/s to ft/min 196.85

        directionRad = 0
        if (dx == 0):
            if (dy > 0):
                directionRad = 3 * np.pi / 2
            elif (dy < 0):
                directionRad = np.pi / 2
        else:
            directionRad = np.arctan(-dy / (dx))
        if dx < 0:
            directionRad += np.pi

        self.direction = directionRad
        # print("("+str(x)+","+str(y)+") "+" ("+str(lastX)+","+str(lastY)+") " + str(directionRad)+"\n")# TODO change this  # Direction in radians

        self.speed = 5 #m/min

        if (data.BURN[rx][ry][1] == 0):
            data.BURN[ry][rx][0] = self.speed
            data.BURN[ry][rx][1] = self.direction
            data.BURN[ry][rx][2] = tick
        # self.preCompute(x,y,p,tick,BURN,A)
            t = threading.Thread(target=self.preCompute, args=(x, y, data, tick))
            t.start()

    def preCompute(self, x, y, data, tick):
        # print(str(tick) +" "+str(x)+" "+str(y)+" \n")
        # print(" (" + str(x) + "," + str(y) + ") \n")
        f = open("output.txt", "a")
        # f.write("("+str(x)+","+str(y)+") "+" ("+str(self.lastX)+","+str(self.lastY)+") " + str(self.direction)+"\n")
        f.write("(" + str(x) + "," + str(y) + ") \n")

        f.close()
        rx = int(self.x / data.p)
        ry = int(self.y / data.p)
        # IMPORTANT: Solely prob model
        for dx, dy in neighborhood:
            if rx + dx >= 0 and ry + dy >= 0 and ry + dy < 6000 and rx + dx < 6000:
                prob = 0.4
                print("wnd:"+str(data.get_windV(self.x,self.y,tick)))
                # TODO: get prob here
                if (np.random.random() <= prob):
                    Fire(x + dx * data.p, y + dy * data.p,data,tick + 1, self.x, self.y)





