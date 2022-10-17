import threading
import time
import numpy as np
from data import *
from rothermelModel import *
from alexandridisModel import *

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
        # print("(" + str(rx) + "," + str(ry) + ")")

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
          # wind 1
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

        if (data.BURN[ry][rx][1] == 0 ):
            data.BURN[ry][rx][0] = self.speed
            data.BURN[ry][rx][2] = self.direction
            data.BURN[ry][rx][1] = tick
         
        # self.preCompute(x,y,p,tick,BURN,A)
            t = threading.Thread(target=self.preCompute, args=(x, y, data, tick))
            t.start()
            

    def preCompute(self, x, y, data, tick):
        # print(str(tick) +" "+str(x)+" "+str(y)+" \n")
        # print(" (" + str(x) + "," + str(y) + ") \n")
        # f = open("output.txt", "a")
        # f.write("("+str(x)+","+str(y)+") "+" ("+str(self.lastX)+","+str(self.lastY)+") " + str(self.direction)+"\n")
        # f.write("(" + str(x) + "," + str(y) + ") \n")

        # f.close()
        rx = int(self.x / data.p)
        ry = int(self.y / data.p)
        # IMPORTANT: Solely prob model
        for dx, dy in neighborhood:
            if rx + dx >= 0 and ry + dy >= 0 and ry + dy < data.nrows and rx + dx < data.ncols:
                
                slope= np.arctan((data.elevation[ry+dy][rx+dx]-data.elevation[ry][rx])/np.sqrt((dx*data.p)**2+(dy*data.p)**2))
                ang=0
                if (dx==1 and dy==1):
                    ang=45
                elif    dx==1 and dy==-1:
                    ang=315
                elif dy==-1 and dx==-1:
                    ang=225
                elif dx==-1 and dy==1:
                    ang=135
                elif dx==1:
                    ang=0
                elif dy==1:
                    ang = 90
                elif dx==-1:
                    ang=180
                elif dy==-1:
                    ang=270

                if data.fuel[ry+dy][rx+dx] == 91:
                    # NB1 - Urban/Developed
                    # NO FIRE SPREAD
                    pveg = -1.0
                    pden = 0.0
                elif data.fuel[ry+dy][rx+dx] == 92:
                    # NB2 - Snow/Ice
                    # NO FIRE SPREAD
                    pveg = -1.0
                    pden = 0.0
                elif data.fuel[ry+dy][rx+dx] == 93:
                    # NB3 - Agricultural
                    # NO FIRE SPREAD
                    pveg = -1.0
                    pden = 0.0
                elif data.fuel[ry+dy][rx+dx] == 98:
                    # NB8 - Open Water
                    # NO FIRE SPREAD
                    pveg = -1.0
                    pden = 0.0
                elif data.fuel[ry+dy][rx+dx] == 99:
                    # NB9 - Barren
                    # NO FIRE SPREAD
                    pveg = -1.0
                    pden = 0.0
                elif data.fuel[ry+dy][rx+dx] == 101:
                    # GR1
                    pveg = 0.4
                    pden = -0.4
                elif data.fuel[ry+dy][rx+dx] == 102:
                    # GR2
                    pveg = 0.4
                    pden = -0.4
                elif data.fuel[ry+dy][rx+dx] == 103:
                    # GR3
                    pveg = 0.4
                    pden = -0.4
                elif data.fuel[ry+dy][rx+dx] == 104:
                    # GR4
                    pveg = 0.4
                    pden = 0.0
                elif data.fuel[ry+dy][rx+dx] == 105:
                    # GR5
                    pveg = 0.4
                    pden = -0.4
                elif data.fuel[ry+dy][rx+dx] == 106:
                    # GR6
                    pveg = 0.4
                    pden = 0.0
                elif data.fuel[ry+dy][rx+dx] == 107:
                    # GR7
                    pveg = 0.4
                    pden = 0.3
                elif data.fuel[ry+dy][rx+dx] == 108:
                    # GR8
                    pveg = 0.4
                    pden = 0.3
                elif data.fuel[ry+dy][rx+dx] == 109:
                    # GR9
                    pveg = 0.4
                    pden = 0.4
                elif data.fuel[ry+dy][rx+dx] == 121:
                    # GS1
                    pveg = 0.4
                    pden = -0.4
                elif data.fuel[ry+dy][rx+dx] == 122:
                    # GS2
                    pveg = 0.4
                    pden = 0.0
                elif data.fuel[ry+dy][rx+dx] == 123:
                    # GS3
                    pveg = 0.4
                    pden = 0.0
                elif data.fuel[ry+dy][rx+dx] == 124:
                    # GS4
                    pveg = 0.4
                    pden = 0.3
                elif data.fuel[ry+dy][rx+dx] == 141:
                    # SH1
                    pveg = 0.4
                    pden = -0.4
                elif data.fuel[ry+dy][rx+dx] == 142:
                    # SH2
                    pveg = 0.4
                    pden = 0.0
                elif data.fuel[ry+dy][rx+dx] == 143:
                    # SH3
                    pveg = 0.4
                    pden = 0.0
                elif data.fuel[ry+dy][rx+dx] == 144:
                    # SH4
                    pveg = 0.4
                    pden = -0.4
                elif data.fuel[ry+dy][rx+dx] == 145:
                    # SH5
                    pveg = 0.4
                    pden = 0.3
                elif data.fuel[ry+dy][rx+dx] == 146:
                    # SH6
                    pveg = 0.4
                    pden = -0.4
                elif data.fuel[ry+dy][rx+dx] == 147:
                    # SH7
                    pveg = 0.4
                    pden = 0.4
                elif data.fuel[ry+dy][rx+dx] == 148:
                    # SH8
                    pveg = 0.4
                    pden = 0.3
                elif data.fuel[ry+dy][rx+dx] == 149:
                    # SH9
                    pveg = 0.4
                    pden = 0.4
                elif data.fuel[ry+dy][rx+dx] == 161:
                    # TU1
                    pveg = 0.4
                    pden = -0.4
                elif data.fuel[ry+dy][rx+dx] == 162:
                    # TU2
                    pveg = 0.4
                    pden = 0.0
                elif data.fuel[ry+dy][rx+dx] == 163:
                    # TU3
                    pveg = 0.4
                    pden = 0.0
                elif data.fuel[ry+dy][rx+dx] == 164:
                    # TU4
                    pveg = 0.4
                    pden = -0.4
                elif data.fuel[ry+dy][rx+dx] == 165:
                    # TU5
                    pveg = 0.4
                    pden = 0.4
                elif data.fuel[ry+dy][rx+dx] == 181:
                    # TL1
                    pveg = 0.4
                    pden = -0.4
                elif data.fuel[ry+dy][rx+dx] == 182:
                    # TL2
                    pveg = 0.4
                    pden = -0.4
                elif data.fuel[ry+dy][rx+dx] == 183:
                    # TL3
                    pveg = 0.1
                    pden = 0.0
                elif data.fuel[ry+dy][rx+dx] == 184:
                    # TL4
                    pveg = 0.2
                    pden = 0.0
                elif data.fuel[ry+dy][rx+dx] == 185:
                    # TL5
                    pveg = 0.2
                    pden = 0.3
                elif data.fuel[ry+dy][rx+dx] == 186:
                    # TL6
                    pveg = 0.4
                    pden = 0.0
                elif data.fuel[ry+dy][rx+dx] == 187:
                    # TL7
                    pveg = 0.2
                    pden = 0.3
                elif data.fuel[ry+dy][rx+dx] == 188:
                    # TL8
                    pveg = 0.4
                    pden = 0.0
                elif data.fuel[ry+dy][rx+dx] == 189:
                    # TL9
                    pveg = 0.4
                    pden = 0.4
                elif data.fuel[ry+dy][rx+dx] == 201:
                    # SB1
                    pveg = 0.4
                    pden = -0.4
                elif data.fuel[ry+dy][rx+dx] == 202:
                    # SB2
                    pveg = 0.4
                    pden = 0.0
                elif data.fuel[ry+dy][rx+dx] == 203:
                    # SB3
                    pveg = 0.4
                    pden = 0.4
                elif data.fuel[ry+dy][rx+dx] == 204:
                    # SB4
                    pveg = 0.5
                    pden = 0.4




                prob=alexandridisModelProbability(slope,ang,data.get_windA(tick,x,y),data.get_windV(tick,x,y),data.p, pveg, pden)
                # print("wnd:"+str(data.get_windV(self.x,self.y,tick)))
                # TODO: get prob here
                if (np.random.random() <= prob):
                    Fire(x + dx * data.p, y + dy * data.p,data,tick + data.p*1.414/(rothermelRate(slope,data.get_windV(tick,x,y))), self.x, self.y)





