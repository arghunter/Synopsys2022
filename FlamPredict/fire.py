import threading
import time
import numpy as np
from numpy import random
from data import *
from rothermelModel import *
from alexandridisModel import *
from rothermelModelSpot import *

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
    #Make stuff around98 100
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

        self.speed = 5  # m/min

        if (data.BURN[ry][rx][1] == 0):
            data.BURN[ry][rx][0] = self.speed
            data.BURN[ry][rx][2] = self.direction
            data.BURN[ry][rx][1] = tick

            # self.preCompute(x,y,p,tick,BURN,A)
            t = threading.Thread(target=self.preCompute, args=(x, y, data, tick))
            t.start()
            # self.preCompute(x,y,data,tick)

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

                slope = np.arctan((data.elevation[ry + dy][rx + dx] - data.elevation[ry][rx]) / np.sqrt(
                    (dx * data.p) ** 2 + (dy * data.p) ** 2))
                ang = 0
                if (dx == 1 and dy == -1):
                    ang = 45
                elif dx == 1 and dy == 1:
                    ang = 315
                elif dy == -1 and dx == 1:
                    ang = 225
                elif dx == -1 and dy == -1:
                    ang = 135
                elif dx == 1:
                    ang = 0
                elif dy == -1:
                    ang = 90
                elif dx == -1:
                    ang = 180
                elif dy == 1:
                    ang = 270

                if data.fuel[ry + dy][rx + dx] == 91:
                    # NB1 - Urban/Developed
                    # NO FIRE SPREAD
                    pveg = -1.0
                    pden = 0.0
                    h = 0  # low heat content (btu/lb)
                    delta = 0  # fuel bed depth (ft)
                    beta = 0.0  # packing ratio (dimentionless)
                    Mx = 0.0  # dead fuel moisture of extinction (fraction)
                    w0 = 0.0  # oven dry fuel load (lb/ft^2)
                    sigma = 0  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 92:
                    # NB2 - Snow/Ice
                    # NO FIRE SPREAD
                    pveg = -1.0
                    pden = 0.0
                    h = 0  # low heat content (btu/lb)
                    delta = 0  # fuel bed depth (ft)
                    beta = 0.0  # packing ratio (dimentionless)
                    Mx = 0.0  # dead fuel moisture of extinction (fraction)
                    w0 = 0.0  # oven dry fuel load (lb/ft^2)
                    sigma = 0  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 93:
                    # NB3 - Agricultural
                    # NO FIRE SPREAD
                    pveg = -1.0
                    pden = 0.0
                    h = 0  # low heat content (btu/lb)
                    delta = 0  # fuel bed depth (ft)
                    beta = 0.0  # packing ratio (dimentionless)
                    Mx = 0.0  # dead fuel moisture of extinction (fraction)
                    w0 = 0.0  # oven dry fuel load (lb/ft^2)
                    sigma = 0  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 98:
                    # NB8 - Open Water
                    # NO FIRE SPREAD
                    pveg = -1.0
                    pden = 0.0
                    h = 0  # low heat content (btu/lb)
                    delta = 0  # fuel bed depth (ft)
                    beta = 0.0  # packing ratio (dimentionless)
                    Mx = 0.0  # dead fuel moisture of extinction (fraction)
                    w0 = 0.0  # oven dry fuel load (lb/ft^2)
                    sigma = 0  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 99:
                    # NB9 - Barren
                    # NO FIRE SPREAD
                    pveg = -1.0
                    pden = 0.0
                    h = 0  # low heat content (btu/lb)
                    delta = 0  # fuel bed depth (ft)
                    beta = 0.0 # packing ratio (dimentionless)
                    Mx = 0.0  # dead fuel moisture of extinction (fraction)
                    w0 = 0.0  # oven dry fuel load (lb/ft^2)
                    sigma = 0  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 100:
                    # NB10 - Next to nb Custom
                    # NO FIRE SPREAD
                    
                    pveg = -1.0
                    pden = 0.0
                    h = 0  # low heat content (btu/lb)
                    delta = 0  # fuel bed depth (ft)
                    beta = 0.0 # packing ratio (dimentionless)
                    Mx = 0.0  # dead fuel moisture of extinction (fraction)
                    w0 = 0.0  # oven dry fuel load (lb/ft^2)
                    sigma = 0  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 101:
                    # GR1
                    pveg = 0.4
                    pden = -0.4
                    h = 8000  # low heat content (btu/lb)
                    delta = 0.4  # fuel bed depth (ft)
                    beta = 0.00143  # packing ratio (dimentionless)
                    Mx = 0.15  # dead fuel moisture of extinction (fraction)
                    w0 = 0.4  # oven dry fuel load (lb/ft^2)
                    sigma = 2054  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 102:
                    # GR2
                    pveg = 0.4
                    pden = -0.4
                    h = 8000  # low heat content (btu/lb)
                    delta = 1.0  # fuel bed depth (ft)
                    beta = 0.00158  # packing ratio (dimentionless)
                    Mx = 0.15  # dead fuel moisture of extinction (fraction)
                    w0 = 1.1  # oven dry fuel load (lb/ft^2)
                    sigma = 1820  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 103:
                    # GR3
                    pveg = 0.4
                    pden = -0.4
                    h = 8000  # low heat content (btu/lb)
                    delta = 2.0  # fuel bed depth (ft)
                    beta = 0.00143  # packing ratio (dimentionless)
                    Mx = 0.3  # dead fuel moisture of extinction (fraction)
                    w0 = 1.6  # oven dry fuel load (lb/ft^2)
                    sigma = 1290  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 104:
                    # GR4
                    pveg = 0.4
                    pden = 0.0
                    h = 8000  # low heat content (btu/lb)
                    delta = 2.0  # fuel bed depth (ft)
                    beta = 0.00154  # packing ratio (dimentionless)
                    Mx = 0.15  # dead fuel moisture of extinction (fraction)
                    w0 = 2.15  # oven dry fuel load (lb/ft^2)
                    sigma = 1826  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 105:
                    # GR5
                    pveg = 0.4
                    pden = -0.4
                    h = 8000  # low heat content (btu/lb)
                    delta = 1.5  # fuel bed depth (ft)
                    beta = 0.00277  # packing ratio (dimentionless)
                    Mx = 0.4  # dead fuel moisture of extinction (fraction)
                    w0 = 2.9  # oven dry fuel load (lb/ft^2)
                    sigma = 1631  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 106:
                    # GR6
                    pveg = 0.4
                    pden = 0.0
                    h = 9000  # low heat content (btu/lb)
                    delta = 1.5  # fuel bed depth (ft)
                    beta = 0.00335  # packing ratio (dimentionless)
                    Mx = 0.4  # dead fuel moisture of extinction (fraction)
                    w0 = 3.5  # oven dry fuel load (lb/ft^2)
                    sigma = 2006  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 107:
                    # GR7
                    pveg = 0.4
                    pden = 0.3
                    h = 8000  # low heat content (btu/lb)
                    delta = 3.0  # fuel bed depth (ft)
                    beta = 0.00306  # packing ratio (dimentionless)
                    Mx = 0.15  # dead fuel moisture of extinction (fraction)
                    w0 = 6.4  # oven dry fuel load (lb/ft^2)
                    sigma = 1834  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 108:
                    # GR8
                    pveg = 0.4
                    pden = 0.3
                    h = 8000  # low heat content (btu/lb)
                    delta = 4.0  # fuel bed depth (ft)
                    beta = 0.00316  # packing ratio (dimentionless)
                    Mx = 0.3  # dead fuel moisture of extinction (fraction)
                    w0 = 7.8  # oven dry fuel load (lb/ft^2)
                    sigma = 1302  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 109:
                    # GR9
                    pveg = 0.4
                    pden = 0.4
                    h = 8000  # low heat content (btu/lb)
                    delta = 5.0  # fuel bed depth (ft)
                    beta = 0.00316  # packing ratio (dimentionless)
                    Mx = 0.4  # dead fuel moisture of extinction (fraction)
                    w0 = 10.0  # oven dry fuel load (lb/ft^2)
                    sigma = 1612  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 121:
                    # GS1
                    pveg = 0.4
                    pden = -0.4
                    h = 8000  # low heat content (btu/lb)
                    delta = 0.9  # fuel bed depth (ft)
                    beta = 0.00215  # packing ratio (dimentionless)
                    Mx = 0.15  # dead fuel moisture of extinction (fraction)
                    w0 = 1.35  # oven dry fuel load (lb/ft^2)
                    sigma = 1832  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 122:
                    # GS2
                    pveg = 0.4
                    pden = 0.0
                    h = 8000  # low heat content (btu/lb)
                    delta = 1.5  # fuel bed depth (ft)
                    beta = 0.00249  # packing ratio (dimentionless)
                    Mx = 0.15  # dead fuel moisture of extinction (fraction)
                    w0 = 2.1  # oven dry fuel load (lb/ft^2)
                    sigma = 1827  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 123:
                    # GS3
                    pveg = 0.4
                    pden = 0.0
                    h = 8000  # low heat content (btu/lb)
                    delta = 1.8  # fuel bed depth (ft)
                    beta = 0.00259  # packing ratio (dimentionless)
                    Mx = 0.4  # dead fuel moisture of extinction (fraction)
                    w0 = 3.0  # oven dry fuel load (lb/ft^2)
                    sigma = 1614  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 124:
                    # GS4
                    pveg = 0.4
                    pden = 0.3
                    h = 8000  # low heat content (btu/lb)
                    delta = 2.1  # fuel bed depth (ft)
                    beta = 0.00874  # packing ratio (dimentionless)
                    Mx = 0.4  # dead fuel moisture of extinction (fraction)
                    w0 = 12.4  # oven dry fuel load (lb/ft^2)
                    sigma = 1674  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 141:
                    # SH1
                    pveg = 0.4
                    pden = -0.4
                    h = 8000  # low heat content (btu/lb)
                    delta = 1.0  # fuel bed depth (ft)
                    beta = 0.00280  # packing ratio (dimentionless)
                    Mx = 0.15  # dead fuel moisture of extinction (fraction)
                    w0 = 1.7  # oven dry fuel load (lb/ft^2)
                    sigma = 1674  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 142:
                    # SH2
                    pveg = 0.4
                    pden = 0.0
                    h = 8000  # low heat content (btu/lb)
                    delta = 1.0  # fuel bed depth (ft)
                    beta = 0.01198  # packing ratio (dimentionless)
                    Mx = 0.15  # dead fuel moisture of extinction (fraction)
                    w0 = 5.2  # oven dry fuel load (lb/ft^2)
                    sigma = 1672  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 143:
                    # SH3
                    pveg = 0.4
                    pden = 0.0
                    h = 8000  # low heat content (btu/lb)
                    delta = 2.4  # fuel bed depth (ft)
                    beta = 0.00577  # packing ratio (dimentionless)
                    Mx = 0.4  # dead fuel moisture of extinction (fraction)
                    w0 = 6.65  # oven dry fuel load (lb/ft^2)
                    sigma = 1371  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 144:
                    # SH4
                    pveg = 0.4
                    pden = -0.4
                    h = 8000  # low heat content (btu/lb)
                    delta = 3.0  # fuel bed depth (ft)
                    beta = 0.00227  # packing ratio (dimentionless)
                    Mx = 0.3  # dead fuel moisture of extinction (fraction)
                    w0 = 3.4  # oven dry fuel load (lb/ft^2)
                    sigma = 1682  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 145:
                    # SH5
                    pveg = 0.4
                    pden = 0.3
                    h = 8000  # low heat content (btu/lb)
                    delta = 6.0  # fuel bed depth (ft)
                    beta = 0.00206  # packing ratio (dimentionless)
                    Mx = 0.15  # dead fuel moisture of extinction (fraction)
                    w0 = 6.5  # oven dry fuel load (lb/ft^2)
                    sigma = 1252  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 146:
                    # SH6
                    pveg = 0.4
                    pden = -0.4
                    h = 8000  # low heat content (btu/lb)
                    delta = 2.0  # fuel bed depth (ft)
                    beta = 0.00412  # packing ratio (dimentionless)
                    Mx = 0.3  # dead fuel moisture of extinction (fraction)
                    w0 = 4.3  # oven dry fuel load (lb/ft^2)
                    sigma = 1144  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 147:
                    # SH7
                    pveg = 0.4
                    pden = 0.4
                    h = 8000  # low heat content (btu/lb)
                    delta = 6.0  # fuel bed depth (ft)
                    beta = 0.00344  # packing ratio (dimentionless)
                    Mx = 0.15  # dead fuel moisture of extinction (fraction)
                    w0 = 6.9  # oven dry fuel load (lb/ft^2)
                    sigma = 1233  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 148:
                    # SH8
                    pveg = 0.4
                    pden = 0.3
                    h = 8000  # low heat content (btu/lb)
                    delta = 3.0  # fuel bed depth (ft)
                    beta = 0.00509  # packing ratio (dimentionless)
                    Mx = 0.4  # dead fuel moisture of extinction (fraction)
                    w0 = 6.4  # oven dry fuel load (lb/ft^2)
                    sigma = 1386  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 149:
                    # SH9
                    pveg = 0.4
                    pden = 0.4
                    h = 8000  # low heat content (btu/lb)
                    delta = 4.4  # fuel bed depth (ft)
                    beta = 0.00505  # packing ratio (dimentionless)
                    Mx = 0.4  # dead fuel moisture of extinction (fraction)
                    w0 = 13.05  # oven dry fuel load (lb/ft^2)
                    sigma = 1378  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 161:
                    # TU1
                    pveg = 0.4
                    pden = -0.4
                    h = 8000  # low heat content (btu/lb)
                    delta = 0.6  # fuel bed depth (ft)
                    beta = 0.00885  # packing ratio (dimentionless)
                    Mx = 0.2  # dead fuel moisture of extinction (fraction)
                    w0 = 1.3  # oven dry fuel load (lb/ft^2)
                    sigma = 1606  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 162:
                    # TU2
                    pveg = 0.4
                    pden = 0.0
                    h = 8000  # low heat content (btu/lb)
                    delta = 1.0  # fuel bed depth (ft)
                    beta = 0.00603  # packing ratio (dimentionless)
                    Mx = 0.3  # dead fuel moisture of extinction (fraction)
                    w0 = 1.15  # oven dry fuel load (lb/ft^2)
                    sigma = 1767  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 163:
                    # TU3
                    pveg = 0.4
                    pden = 0.0
                    h = 8000  # low heat content (btu/lb)
                    delta = 1.3  # fuel bed depth (ft)
                    beta = 0.00359  # packing ratio (dimentionless)
                    Mx = 0.3  # dead fuel moisture of extinction (fraction)
                    w0 = 2.85  # oven dry fuel load (lb/ft^2)
                    sigma = 1611  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 164:
                    # TU4
                    pveg = 0.4
                    pden = -0.4
                    h = 8000  # low heat content (btu/lb)
                    delta = 0.5  # fuel bed depth (ft)
                    beta = 0.01865  # packing ratio (dimentionless)
                    Mx = 0.12  # dead fuel moisture of extinction (fraction)
                    w0 = 6.5  # oven dry fuel load (lb/ft^2)
                    sigma = 2216  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 165:
                    # TU5
                    pveg = 0.4
                    pden = 0.4
                    h = 8000  # low heat content (btu/lb)
                    delta = 1.0  # fuel bed depth (ft)
                    beta = 0.02009  # packing ratio (dimentionless)
                    Mx = 0.25  # dead fuel moisture of extinction (fraction)
                    w0 = 7.0  # oven dry fuel load (lb/ft^2)
                    sigma = 1224  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 181:
                    # TL1
                    pveg = 0.4
                    pden = -0.4
                    h = 8000  # low heat content (btu/lb)
                    delta = 0.2  # fuel bed depth (ft)
                    beta = 0.04878  # packing ratio (dimentionless)
                    Mx = 0.3  # dead fuel moisture of extinction (fraction)
                    w0 = 1.0  # oven dry fuel load (lb/ft^2)
                    sigma = 1716  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 182:
                    # TL2
                    pveg = 0.4
                    pden = -0.4
                    h = 8000  # low heat content (btu/lb)
                    delta = 0.2  # fuel bed depth (ft)
                    beta = 0.04232  # packing ratio (dimentionless)
                    Mx = 0.25  # dead fuel moisture of extinction (fraction)
                    w0 = 1.4  # oven dry fuel load (lb/ft^2)
                    sigma = 1806  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 183:
                    # TL3
                    pveg = 0.1
                    pden = 0.0
                    h = 8000  # low heat content (btu/lb)
                    delta = 0.3  # fuel bed depth (ft)
                    beta = 0.02630  # packing ratio (dimentionless)
                    Mx = 0.2  # dead fuel moisture of extinction (fraction)
                    w0 = 0.5  # oven dry fuel load (lb/ft^2)
                    sigma = 1532  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 184:
                    # TL4
                    pveg = 0.2
                    pden = 0.0
                    h = 8000  # low heat content (btu/lb)
                    delta = 0.4  # fuel bed depth (ft)
                    beta = 0.02224  # packing ratio (dimentionless)
                    Mx = 0.25  # dead fuel moisture of extinction (fraction)
                    w0 = 0.5  # oven dry fuel load (lb/ft^2)
                    sigma = 1568  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 185:
                    # TL5
                    pveg = 0.2
                    pden = 0.3
                    h = 8000  # low heat content (btu/lb)
                    delta = 0.6  # fuel bed depth (ft)
                    beta = 0.01925  # packing ratio (dimentionless)
                    Mx = 0.25  # dead fuel moisture of extinction (fraction)
                    w0 = 1.15  # oven dry fuel load (lb/ft^2)
                    sigma = 1713  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 186:
                    # TL6
                    pveg = 0.4
                    pden = 0.0
                    h = 8000  # low heat content (btu/lb)
                    delta = 0.3  # fuel bed depth (ft)
                    beta = 0.02296  # packing ratio (dimentionless)
                    Mx = 0.25  # dead fuel moisture of extinction (fraction)
                    w0 = 2.4  # oven dry fuel load (lb/ft^2)
                    sigma = 1936  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 187:
                    # TL7
                    pveg = 0.2
                    pden = 0.3
                    h = 8000  # low heat content (btu/lb)
                    delta = 0.4  # fuel bed depth (ft)
                    beta = 0.03515  # packing ratio (dimentionless)
                    Mx = 0.25  # dead fuel moisture of extinction (fraction)
                    w0 = 0.3  # oven dry fuel load (lb/ft^2)
                    sigma = 1229  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 188:
                    # TL8
                    pveg = 0.4
                    pden = 0.0
                    h = 8000  # low heat content (btu/lb)
                    delta = 0.3  # fuel bed depth (ft)
                    beta = 0.03969  # packing ratio (dimentionless)
                    Mx = 0.35  # dead fuel moisture of extinction (fraction)
                    w0 = 5.8  # oven dry fuel load (lb/ft^2)
                    sigma = 1770  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 189:
                    # TL9
                    pveg = 0.4
                    pden = 0.4
                    h = 8000  # low heat content (btu/lb)
                    delta = 0.6  # fuel bed depth (ft)
                    beta = 0.03372  # packing ratio (dimentionless)
                    Mx = 0.35  # dead fuel moisture of extinction (fraction)
                    w0 = 6.65  # oven dry fuel load (lb/ft^2)
                    sigma = 1733  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 201:
                    # SB1
                    pveg = 0.4
                    pden = -0.4
                    h = 8000  # low heat content (btu/lb)
                    delta = 1.0  # fuel bed depth (ft)
                    beta = 0.02224  # packing ratio (dimentionless)
                    Mx = 0.25  # dead fuel moisture of extinction (fraction)
                    w0 = 1.5  # oven dry fuel load (lb/ft^2)
                    sigma = 1653  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 202:
                    # SB2
                    pveg = 0.4
                    pden = 0.0
                    h = 8000  # low heat content (btu/lb)
                    delta = 1.0  # fuel bed depth (ft)
                    beta = 0.01829  # packing ratio (dimentionless)
                    Mx = 0.25  # dead fuel moisture of extinction (fraction)
                    w0 = 4.5  # oven dry fuel load (lb/ft^2)
                    sigma = 1884  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 203:
                    # SB3
                    pveg = 0.4
                    pden = 0.4
                    h = 8000  # low heat content (btu/lb)
                    delta = 1.2  # fuel bed depth (ft)
                    beta = 0.01345  # packing ratio (dimentionless)
                    Mx = 0.25  # dead fuel moisture of extinction (fraction)
                    w0 = 5.5  # oven dry fuel load (lb/ft^2)
                    sigma = 1935  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                elif data.fuel[ry + dy][rx + dx] == 204:
                    # SB4
                    pveg = 0.5
                    pden = 0.4
                    h = 8000  # low heat content (btu/lb)
                    delta = 2.7  # fuel bed depth (ft)
                    beta = 0.00744  # packing ratio (dimentionless)
                    Mx = 0.25  # dead fuel moisture of extinction (fraction)
                    w0 = 5.25  # oven dry fuel load (lb/ft^2)
                    sigma = 1907  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                else:
                    pveg = -1.0
                    pden = 0.0
                    h = 0  # low heat content (btu/lb)
                    delta = 0  # fuel bed depth (ft)
                    beta = 0.0  # packing ratio (dimentionless)
                    Mx = 0.0  # dead fuel moisture of extinction (fraction)
                    w0 = 0.0  # oven dry fuel load (lb/ft^2)
                    sigma = 0  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                

                prob = alexandridisModelProbability(slope, ang, data.get_windA(tick, x, y), data.get_windV(tick, x, y), pveg, pden)
                # print("wnd:"+str(data.get_windV(self.x,self.y,tick)))
                # TODO: get prob here
                if (0.5 <= prob):
                    # Fire(x + dx * data.p, y + dy * data.p,data,tick+1, self.x, self.y)
                    tanPhi = slope
                    Uroth= ((data.get_windV(tick, x, y)*3.28084)*60)
                    rothThetawf = (data.get_windA(tick, x, y) - ang)
                    rothrThetawf = (np.pi - math.radians(rothThetawf))
                    realUmult = math.cos(rothrThetawf)
                    realU = (Uroth*realUmult)
                    R = ((rothermelRate(tanPhi, realU, h, delta, beta, Mx, w0, sigma))/data.p)
                    # print("R val", R)
                    tsR = (1/R)
                    # print("tsR", tsR)

                    # print("R val", R)
                    # data.p = side length
                    # Fire(x + dx * data.p, y + dy * data.p, data, tick + (data.p * (1.414 / R)), self.x, self.y)
                    # Fire(x + dx * data.p, y + dy * data.p, data, tick + R, self.x, self.y)
                    Fire(x + dx * data.p, y + dy * data.p, data, int(tick+tsR), self.x, self.y)


                ##################################################################
                # spotting

            lambdaVal = 1  # lambda for poisson for Number of spotting items #TODO: find value
            Nsubp = int(random.poisson(lam=lambdaVal, size=None))  # number of spotting cells from poisson dist
            # info: size= None gives one scalar value

            rnMeanVal = 2  # mean val for rn from gaussian dist #TODO: find val
            rnStdVal = 2  # std val for rn from gaussian dist #TODO: find val

            # spotting

            # random spot direction #TODO: improve later
            spotAngOptionsX = [-4, -3, -2, -1, 0, 1, 2, 3, 4]  # in 9x9 grid, relative to center tile
            spotAngOptionsY = [-4, -3, -2, -1, 0, 1, 2, 3, 4]  # in 9x9 grid, relative to center tile
            spotAngOptionsY2 = [-4, -3, -2, -1, 1, 2, 3, 4]  # in 9x9 grid, relative to center tile, if 0 and 0 then pull Y from this
            for i in range(Nsubp):
                spotAngX = random.choice(spotAngOptionsX)  # for generating random angle, spot in X
                spotAngY = random.choice(spotAngOptionsY)  # for generating random angle, spot in Y

                if spotAngX == 0 and spotAngY == 0:
                    spotAngY = random.choice(spotAngOptionsY2)  # rerolling AngY so not on the same point
                    # this process is statistically correct because Nsubp guarantees spotting of 2 cells, if on same cell, then Nsubp condition not met

                if spotAngX > 0 and spotAngY > 0:
                    rangSpot = math.atan((spotAngY / spotAngX))
                elif spotAngX > 0 and spotAngY < 0:
                    rangSpot = ((2 * math.pi) + math.atan((spotAngY / spotAngX)))
                elif spotAngX < 0 and spotAngY > 0:
                    rangSpot = (math.pi + math.atan((spotAngY / spotAngX)))
                elif spotAngX < 0 and spotAngY < 0:
                    rangSpot = (math.pi + math.atan((spotAngY / spotAngX)))
                elif spotAngX == 0 and spotAngY > 0:
                    rangSpot = (math.pi / 2)
                elif spotAngX == 0 and spotAngY < 0:
                    rangSpot = (((3 * math.pi) / 2))
                else:
                    rangSpot = math.atan((spotAngY / spotAngX)) #TODO: fix rangspot not defined error

                # spotting distance

                # generated random rn from gaussian distribution
                rsubn = float(random.normal(loc=rnMeanVal, scale=rnStdVal, size=None))  # TODO: tune vals
                # info: size = None gives one scalar value
                # info: loc = mean
                # info: scale = std

                # relative wind angle
                thetawSpot = data.get_windA(tick, x, y)
                Uspot = (data.get_windV(tick, x, y))
                thetawfSpot = (thetawSpot - rangSpot)
                rthetawfSpot = (math.pi - math.radians(thetawfSpot))

                # spotting distance (cells)
                spotDistance = (rsubn * math.exp((Uspot * (math.cos(rthetawfSpot) - 1))))
                spotDistX = (spotDistance * (math.cos(rangSpot)))
                spotDistY = (spotDistance * (math.sin(rangSpot)))

                # real x,y, spotting distance (cells), statistically correct because inherently random
                if Uspot > 0 and rthetawfSpot > 0:
                    if spotDistX > 0:
                        realspotDistX = int(math.ceil(spotDistX))
                    elif spotDistX < 0:
                        realspotDistX = int(math.floor(spotDistX))
                    elif spotDistX == 0:
                        realspotDistX = int(round(spotDistX))
                    if spotDistY > 0:
                        realspotDistY = int(math.ceil(spotDistY))
                    elif spotDistY < 0:
                        realspotDistY = int(math.floor(spotDistY))
                    elif spotDistY == 0:
                        realspotDistY = int(round(spotDistY))
                elif Uspot < 0 and rthetawfSpot > 0:
                    if spotDistX > 0:
                        realspotDistX = int(math.floor(spotDistX))
                    elif spotDistX < 0:
                        realspotDistX = int(math.ceil(spotDistX))
                    elif spotDistX == 0:
                        realspotDistX = int(round(spotDistX))
                    if spotDistY > 0:
                        realspotDistY = int(math.floor(spotDistY))
                    elif spotDistY < 0:
                        realspotDistY = int(math.ceil(spotDistY))
                    elif spotDistY == 0:
                        realspotDistY = int(round(spotDistY))
                elif Uspot > 0 and rthetawfSpot < 0:
                    if spotDistX > 0:
                        realspotDistX = int(math.floor(spotDistX))
                    elif spotDistX < 0:
                        realspotDistX = int(math.ceil(spotDistX))
                    elif spotDistX == 0:
                        realspotDistX = int(round(spotDistX))
                    if spotDistY > 0:
                        realspotDistY = int(math.floor(spotDistY))
                    elif spotDistY < 0:
                        realspotDistY = int(math.ceil(spotDistY))
                    elif spotDistY == 0:
                        realspotDistY = int(round(spotDistY))
                elif Uspot < 0 and rthetawfSpot < 0:
                    if spotDistX > 0:
                        realspotDistX = int(math.ceil(spotDistX))
                    elif spotDistX < 0:
                        realspotDistX = int(math.floor(spotDistX))
                    elif spotDistX == 0:
                        realspotDistX = int(round(spotDistX))
                    if spotDistY > 0:
                        realspotDistY = int(math.ceil(spotDistY))
                    elif spotDistY < 0:
                        realspotDistY = int(math.floor(spotDistY))
                    elif spotDistY == 0:
                        realspotDistY = int(round(spotDistY))
                else:
                    realspotDistX = int(round(spotDistX))
                    realspotDistY = int(round(spotDistY))
                if rx + realspotDistX >= 0 and ry + realspotDistY >= 0 and ry + realspotDistY < data.nrows and rx + realspotDistX < data.ncols:


                    # fuel values for spotted cell
                    if data.fuel[ry + realspotDistY][rx + realspotDistX] == 91:
                        # NB1 - Urban/Developed
                        # NO FIRE SPREAD
                        pvegSpot = -1.0
                        pdenSpot = 0.0
                        hSpot = 0  # low hSpoteat content (btu/lb)
                        deltaSpot = 0  # fuel bed depthSpot (ft)
                        betaSpot = 0.0  # packing ratio (dimentionless)
                        MxSpot = 0.0  # dead fuel moisture of extinction (fraction)
                        w0Spot = 0.0  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 0  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 92:
                        # NB2 - Snow/Ice
                        # NO FIRE SPREAD
                        pvegSpot = -1.0
                        pdenSpot = 0.0
                        hSpot = 0  # low hSpoteat content (btu/lb)
                        deltaSpot = 0  # fuel bed depthSpot (ft)
                        betaSpot = 0.0  # packing ratio (dimentionless)
                        MxSpot = 0.0  # dead fuel moisture of extinction (fraction)
                        w0Spot = 0.0  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 0  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 93:
                        # NB3 - Agricultural
                        # NO FIRE SPREAD
                        pvegSpot = -1.0
                        pdenSpot = 0.0
                        hSpot = 0  # low hSpoteat content (btu/lb)
                        deltaSpot = 0  # fuel bed depthSpot (ft)
                        betaSpot = 0.0  # packing ratio (dimentionless)
                        MxSpot = 0.0  # dead fuel moisture of extinction (fraction)
                        w0Spot = 0.0  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 0  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 98:
                        # NB8 - Open Water
                        # NO FIRE SPREAD
                        pvegSpot = -1.0
                        pdenSpot = 0.0
                        hSpot = 0  # low hSpoteat content (btu/lb)
                        deltaSpot = 0  # fuel bed depthSpot (ft)
                        betaSpot = 0.0  # packing ratio (dimentionless)
                        MxSpot = 0.0  # dead fuel moisture of extinction (fraction)
                        w0Spot = 0.0  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 0  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 99:
                        # NB9 - Barren
                        # NO FIRE SPREAD
                        pvegSpot = -1.0
                        pdenSpot = 0.0
                        hSpot = 0  # low hSpoteat content (btu/lb)
                        deltaSpot = 0  # fuel bed depthSpot (ft)
                        betaSpot = 0.0  # packing ratio (dimentionless)
                        MxSpot = 0.0  # dead fuel moisture of extinction (fraction)
                        w0Spot = 0.0  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 0  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 100:
                        # NB10 - Next to nb Custom
                        # NO FIRE SPREAD

                        pvegSpot = -1.0
                        pdenSpot = 0.0
                        hSpot = 0  # low hSpoteat content (btu/lb)
                        deltaSpot = 0  # fuel bed depthSpot (ft)
                        betaSpot = 0.0  # packing ratio (dimentionless)
                        MxSpot = 0.0  # dead fuel moisture of extinction (fraction)
                        w0Spot = 0.0  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 0  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 101:
                        # GR1
                        pvegSpot = 0.4
                        pdenSpot = -0.4
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 0.4  # fuel bed depthSpot (ft)
                        betaSpot = 0.00143  # packing ratio (dimentionless)
                        MxSpot = 0.15  # dead fuel moisture of extinction (fraction)
                        w0Spot = 0.4  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 2054  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 102:
                        # GR2
                        pvegSpot = 0.4
                        pdenSpot = -0.4
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 1.0  # fuel bed depthSpot (ft)
                        betaSpot = 0.00158  # packing ratio (dimentionless)
                        MxSpot = 0.15  # dead fuel moisture of extinction (fraction)
                        w0Spot = 1.1  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1820  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 103:
                        # GR3
                        pvegSpot = 0.4
                        pdenSpot = -0.4
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 2.0  # fuel bed depthSpot (ft)
                        betaSpot = 0.00143  # packing ratio (dimentionless)
                        MxSpot = 0.3  # dead fuel moisture of extinction (fraction)
                        w0Spot = 1.6  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1290  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 104:
                        # GR4
                        pvegSpot = 0.4
                        pdenSpot = 0.0
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 2.0  # fuel bed depthSpot (ft)
                        betaSpot = 0.00154  # packing ratio (dimentionless)
                        MxSpot = 0.15  # dead fuel moisture of extinction (fraction)
                        w0Spot = 2.15  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1826  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 105:
                        # GR5
                        pvegSpot = 0.4
                        pdenSpot = -0.4
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 1.5  # fuel bed depthSpot (ft)
                        betaSpot = 0.00277  # packing ratio (dimentionless)
                        MxSpot = 0.4  # dead fuel moisture of extinction (fraction)
                        w0Spot = 2.9  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1631  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 106:
                        # GR6
                        pvegSpot = 0.4
                        pdenSpot = 0.0
                        hSpot = 9000  # low hSpoteat content (btu/lb)
                        deltaSpot = 1.5  # fuel bed depthSpot (ft)
                        betaSpot = 0.00335  # packing ratio (dimentionless)
                        MxSpot = 0.4  # dead fuel moisture of extinction (fraction)
                        w0Spot = 3.5  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 2006  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 107:
                        # GR7
                        pvegSpot = 0.4
                        pdenSpot = 0.3
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 3.0  # fuel bed depthSpot (ft)
                        betaSpot = 0.00306  # packing ratio (dimentionless)
                        MxSpot = 0.15  # dead fuel moisture of extinction (fraction)
                        w0Spot = 6.4  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1834  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 108:
                        # GR8
                        pvegSpot = 0.4
                        pdenSpot = 0.3
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 4.0  # fuel bed depthSpot (ft)
                        betaSpot = 0.00316  # packing ratio (dimentionless)
                        MxSpot = 0.3  # dead fuel moisture of extinction (fraction)
                        w0Spot = 7.8  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1302  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 109:
                        # GR9
                        pvegSpot = 0.4
                        pdenSpot = 0.4
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 5.0  # fuel bed depthSpot (ft)
                        betaSpot = 0.00316  # packing ratio (dimentionless)
                        MxSpot = 0.4  # dead fuel moisture of extinction (fraction)
                        w0Spot = 10.0  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1612  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 121:
                        # GS1
                        pvegSpot = 0.4
                        pdenSpot = -0.4
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 0.9  # fuel bed depthSpot (ft)
                        betaSpot = 0.00215  # packing ratio (dimentionless)
                        MxSpot = 0.15  # dead fuel moisture of extinction (fraction)
                        w0Spot = 1.35  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1832  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 122:
                        # GS2
                        pvegSpot = 0.4
                        pdenSpot = 0.0
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 1.5  # fuel bed depthSpot (ft)
                        betaSpot = 0.00249  # packing ratio (dimentionless)
                        MxSpot = 0.15  # dead fuel moisture of extinction (fraction)
                        w0Spot = 2.1  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1827  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 123:
                        # GS3
                        pvegSpot = 0.4
                        pdenSpot = 0.0
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 1.8  # fuel bed depthSpot (ft)
                        betaSpot = 0.00259  # packing ratio (dimentionless)
                        MxSpot = 0.4  # dead fuel moisture of extinction (fraction)
                        w0Spot = 3.0  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1614  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 124:
                        # GS4
                        pvegSpot = 0.4
                        pdenSpot = 0.3
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 2.1  # fuel bed depthSpot (ft)
                        betaSpot = 0.00874  # packing ratio (dimentionless)
                        MxSpot = 0.4  # dead fuel moisture of extinction (fraction)
                        w0Spot = 12.4  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1674  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 141:
                        # ShSpot1
                        pvegSpot = 0.4
                        pdenSpot = -0.4
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 1.0  # fuel bed depthSpot (ft)
                        betaSpot = 0.00280  # packing ratio (dimentionless)
                        MxSpot = 0.15  # dead fuel moisture of extinction (fraction)
                        w0Spot = 1.7  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1674  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 142:
                        # ShSpot2
                        pvegSpot = 0.4
                        pdenSpot = 0.0
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 1.0  # fuel bed depthSpot (ft)
                        betaSpot = 0.01198  # packing ratio (dimentionless)
                        MxSpot = 0.15  # dead fuel moisture of extinction (fraction)
                        w0Spot = 5.2  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1672  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 143:
                        # ShSpot3
                        pvegSpot = 0.4
                        pdenSpot = 0.0
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 2.4  # fuel bed depthSpot (ft)
                        betaSpot = 0.00577  # packing ratio (dimentionless)
                        MxSpot = 0.4  # dead fuel moisture of extinction (fraction)
                        w0Spot = 6.65  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1371  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 144:
                        # ShSpot4
                        pvegSpot = 0.4
                        pdenSpot = -0.4
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 3.0  # fuel bed depthSpot (ft)
                        betaSpot = 0.00227  # packing ratio (dimentionless)
                        MxSpot = 0.3  # dead fuel moisture of extinction (fraction)
                        w0Spot = 3.4  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1682  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 145:
                        # ShSpot5
                        pvegSpot = 0.4
                        pdenSpot = 0.3
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 6.0  # fuel bed depthSpot (ft)
                        betaSpot = 0.00206  # packing ratio (dimentionless)
                        MxSpot = 0.15  # dead fuel moisture of extinction (fraction)
                        w0Spot = 6.5  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1252  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 146:
                        # ShSpot6
                        pvegSpot = 0.4
                        pdenSpot = -0.4
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 2.0  # fuel bed depthSpot (ft)
                        betaSpot = 0.00412  # packing ratio (dimentionless)
                        MxSpot = 0.3  # dead fuel moisture of extinction (fraction)
                        w0Spot = 4.3  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1144  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 147:
                        # ShSpot7
                        pvegSpot = 0.4
                        pdenSpot = 0.4
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 6.0  # fuel bed depthSpot (ft)
                        betaSpot = 0.00344  # packing ratio (dimentionless)
                        MxSpot = 0.15  # dead fuel moisture of extinction (fraction)
                        w0Spot = 6.9  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1233  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 148:
                        # ShSpot8
                        pvegSpot = 0.4
                        pdenSpot = 0.3
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 3.0  # fuel bed depthSpot (ft)
                        betaSpot = 0.00509  # packing ratio (dimentionless)
                        MxSpot = 0.4  # dead fuel moisture of extinction (fraction)
                        w0Spot = 6.4  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1386  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 149:
                        # ShSpot9
                        pvegSpot = 0.4
                        pdenSpot = 0.4
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 4.4  # fuel bed depthSpot (ft)
                        betaSpot = 0.00505  # packing ratio (dimentionless)
                        MxSpot = 0.4  # dead fuel moisture of extinction (fraction)
                        w0Spot = 13.05  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1378  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 161:
                        # TU1
                        pvegSpot = 0.4
                        pdenSpot = -0.4
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 0.6  # fuel bed depthSpot (ft)
                        betaSpot = 0.00885  # packing ratio (dimentionless)
                        MxSpot = 0.2  # dead fuel moisture of extinction (fraction)
                        w0Spot = 1.3  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1606  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 162:
                        # TU2
                        pvegSpot = 0.4
                        pdenSpot = 0.0
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 1.0  # fuel bed depthSpot (ft)
                        betaSpot = 0.00603  # packing ratio (dimentionless)
                        MxSpot = 0.3  # dead fuel moisture of extinction (fraction)
                        w0Spot = 1.15  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1767  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 163:
                        # TU3
                        pvegSpot = 0.4
                        pdenSpot = 0.0
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 1.3  # fuel bed depthSpot (ft)
                        betaSpot = 0.00359  # packing ratio (dimentionless)
                        MxSpot = 0.3  # dead fuel moisture of extinction (fraction)
                        w0Spot = 2.85  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1611  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 164:
                        # TU4
                        pvegSpot = 0.4
                        pdenSpot = -0.4
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 0.5  # fuel bed depthSpot (ft)
                        betaSpot = 0.01865  # packing ratio (dimentionless)
                        MxSpot = 0.12  # dead fuel moisture of extinction (fraction)
                        w0Spot = 6.5  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 2216  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 165:
                        # TU5
                        pvegSpot = 0.4
                        pdenSpot = 0.4
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 1.0  # fuel bed depthSpot (ft)
                        betaSpot = 0.02009  # packing ratio (dimentionless)
                        MxSpot = 0.25  # dead fuel moisture of extinction (fraction)
                        w0Spot = 7.0  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1224  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 181:
                        # TL1
                        pvegSpot = 0.4
                        pdenSpot = -0.4
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 0.2  # fuel bed depthSpot (ft)
                        betaSpot = 0.04878  # packing ratio (dimentionless)
                        MxSpot = 0.3  # dead fuel moisture of extinction (fraction)
                        w0Spot = 1.0  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1716  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 182:
                        # TL2
                        pvegSpot = 0.4
                        pdenSpot = -0.4
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 0.2  # fuel bed depthSpot (ft)
                        betaSpot = 0.04232  # packing ratio (dimentionless)
                        MxSpot = 0.25  # dead fuel moisture of extinction (fraction)
                        w0Spot = 1.4  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1806  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 183:
                        # TL3
                        pvegSpot = 0.1
                        pdenSpot = 0.0
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 0.3  # fuel bed depthSpot (ft)
                        betaSpot = 0.02630  # packing ratio (dimentionless)
                        MxSpot = 0.2  # dead fuel moisture of extinction (fraction)
                        w0Spot = 0.5  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1532  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 184:
                        # TL4
                        pvegSpot = 0.2
                        pdenSpot = 0.0
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 0.4  # fuel bed depthSpot (ft)
                        betaSpot = 0.02224  # packing ratio (dimentionless)
                        MxSpot = 0.25  # dead fuel moisture of extinction (fraction)
                        w0Spot = 0.5  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1568  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 185:
                        # TL5
                        pvegSpot = 0.2
                        pdenSpot = 0.3
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 0.6  # fuel bed depthSpot (ft)
                        betaSpot = 0.01925  # packing ratio (dimentionless)
                        MxSpot = 0.25  # dead fuel moisture of extinction (fraction)
                        w0Spot = 1.15  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1713  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 186:
                        # TL6
                        pvegSpot = 0.4
                        pdenSpot = 0.0
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 0.3  # fuel bed depthSpot (ft)
                        betaSpot = 0.02296  # packing ratio (dimentionless)
                        MxSpot = 0.25  # dead fuel moisture of extinction (fraction)
                        w0Spot = 2.4  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1936  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 187:
                        # TL7
                        pvegSpot = 0.2
                        pdenSpot = 0.3
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 0.4  # fuel bed depthSpot (ft)
                        betaSpot = 0.03515  # packing ratio (dimentionless)
                        MxSpot = 0.25  # dead fuel moisture of extinction (fraction)
                        w0Spot = 0.3  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1229  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 188:
                        # TL8
                        pvegSpot = 0.4
                        pdenSpot = 0.0
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 0.3  # fuel bed depthSpot (ft)
                        betaSpot = 0.03969  # packing ratio (dimentionless)
                        MxSpot = 0.35  # dead fuel moisture of extinction (fraction)
                        w0Spot = 5.8  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1770  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 189:
                        # TL9
                        pvegSpot = 0.4
                        pdenSpot = 0.4
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 0.6  # fuel bed depthSpot (ft)
                        betaSpot = 0.03372  # packing ratio (dimentionless)
                        MxSpot = 0.35  # dead fuel moisture of extinction (fraction)
                        w0Spot = 6.65  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1733  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 201:
                        # SB1
                        pvegSpot = 0.4
                        pdenSpot = -0.4
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 1.0  # fuel bed depthSpot (ft)
                        betaSpot = 0.02224  # packing ratio (dimentionless)
                        MxSpot = 0.25  # dead fuel moisture of extinction (fraction)
                        w0Spot = 1.5  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1653  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 202:
                        # SB2
                        pvegSpot = 0.4
                        pdenSpot = 0.0
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 1.0  # fuel bed depthSpot (ft)
                        betaSpot = 0.01829  # packing ratio (dimentionless)
                        MxSpot = 0.25  # dead fuel moisture of extinction (fraction)
                        w0Spot = 4.5  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1884  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 203:
                        # SB3
                        pvegSpot = 0.4
                        pdenSpot = 0.4
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 1.2  # fuel bed depthSpot (ft)
                        betaSpot = 0.01345  # packing ratio (dimentionless)
                        MxSpot = 0.25  # dead fuel moisture of extinction (fraction)
                        w0Spot = 5.5  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1935  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    elif data.fuel[ry + realspotDistY][rx + realspotDistX] == 204:
                        # SB4
                        pvegSpot = 0.5
                        pdenSpot = 0.4
                        hSpot = 8000  # low hSpoteat content (btu/lb)
                        deltaSpot = 2.7  # fuel bed depthSpot (ft)
                        betaSpot = 0.00744  # packing ratio (dimentionless)
                        MxSpot = 0.25  # dead fuel moisture of extinction (fraction)
                        w0Spot = 5.25  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 1907  # Surface-area-to-volume ratio of tree (ft^2/ft^3)
                    else:
                        pvegSpot = -1.0
                        pdenSpot = 0.0
                        hSpot = 0  # low hSpoteat content (btu/lb)
                        deltaSpot = 0  # fuel bed depthSpot (ft)
                        betaSpot = 0.0  # packing ratio (dimentionless)
                        MxSpot = 0.0  # dead fuel moisture of extinction (fraction)
                        w0Spot = 0.0  # oven dry fuel load (lb/ft^2)
                        sigmaSpot = 0  # Surface-area-to-volume ratio of tree (ft^2/ft^3)

                    # probability that spotted cell will burn, found using Alexandridis model using pveg and pden
                    # disregard slope and wind in calculating burn prob of spotted cell b/c spot from top
                    phSpot = 0.58  # pre optimised
                    Pc = (phSpot * (1 + pvegSpot) * (1 + pdenSpot))

                    if (0.5 <= Pc):
                        Rspot = ((rothermelRateSpot(0, 0, hSpot, deltaSpot, betaSpot, MxSpot, w0Spot, sigmaSpot))/data.p)
                        # unit conversion
                        # print("R val", R)
                        tsRSpot = (1 / Rspot)
                        # print("tsR", tsR)

                        # print("R val", R)
                        # data.p = side length
                        # Fire(x + dx * data.p, y + dy * data.p, data, tick + (data.p * (1.414 / R)), self.x, self.y)
                        # Fire(x + dx * data.p, y + dy * data.p, data, tick + R, self.x, self.y)
                        Fire(x + realspotDistX * data.p, y + realspotDistY * data.p, data, int(tick + tsRSpot), self.x, self.y)


                    

