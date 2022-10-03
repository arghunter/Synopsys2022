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

            # altitude of spread to cell
            z2 = (A[ry][rx])
            # altitude of current cell
            z1 = (A[rlastY][rlastX])
            # delta = z diff
            dz = float(z2-z1)
            rdz = float(round(dz, 10))

            x2 = (rx)  # x2
            x1 = (rlastX)  # x1
            dx = (x2 - x1)
            sdx = ((dx) ** 2)
            y2 = (ry)  # y2
            y1 = (rlastY)  # y1
            dy = (y2 - y1)
            sdy = ((dy) ** 2)

            # 2d distance = dxy
            dxy = np.sqrt((sdx + sdy))
            rdxy = float(round(dxy, 10))

            # 3d slope between (x1,y1,z1), (x2,y2,z2)
            Phi = (float(rdz / rdxy) * 100)
            print("slope %", Phi)

            # wind velocity at midflame height (ft/min)
            U = 1 # wind 1

            # m/s to ft/min 196.85


            directionRad = np.arctan(dy/dx)
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
        print(" (" + str(x) + "," + str(y) + ") \n")
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




