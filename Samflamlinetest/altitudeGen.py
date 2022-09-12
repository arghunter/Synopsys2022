import time
from tkinter.tix import Tree
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import animation
from matplotlib import colors
from queue import Queue
import threading
import random


class valueA:

    nx, ny = 1024, 1024

    valAlt = np.zeros((ny, nx))

    altitude_vari = 0.5
    @staticmethod
    def popAltSeg(A, ix, iy):
        A[iy][ix] = 1

        # if(np.random.random() < 0.3):
        #     A[iy][ix] = -1

        # print("Altitude"+str(ix)+" "+str(iy))
        # print("("+str(ix)+","+str(iy)+")")

        A[iy][ix] = A[iy][ix] * 240 * np.random.random() + 80 * A[iy][ix]
        # d = np.random.random()*200

        for tx in range(ix - 80, ix + 80):
            # print(tx-ix)
            for ty in range(iy - 80, iy + 80):

                if ((tx - ix) ** 2 + (ty - iy) ** 2 <= (80) ** 2 and A[ty][tx] != 1):

                    if (A[iy][ix] < 0):
                        t = A[iy][ix] + \
                            (abs(tx - ix) + abs(ty - tx)) / 2
                        A[ty][tx] -= abs(t)
                    else:
                        t = A[iy][ix] - \
                            (abs(tx - ix) + abs(ty - tx)) / 2
                        A[ty][tx] += abs(t)

                        # if(t >= 0):
                        #     A[ty][tx] += t

                    if A[ty][tx] == 1:
                        A[ty][tx] = 2
                        # print("("+str(ty)+","+str(tx)+")")
                        # print(str(iy)+" "+str(ix) + " " + str(ty) +
                        #       " "+str(tx)+" "+str(A[ty][tx]))
        A[1023][1023] = A[1023][1023] - 1

    @staticmethod
    def popAltitude(A):
        tc = 0
        for i in range(0, 1024):
            tc += 1
            tx = int(random.random() * (valueA.nx - 160)) + 80
            ty = int(random.random() * (valueA.ny - 160)) + 80
            t = (threading.Thread(target=valueA.popAltSeg, args=(
                A, tx, ty)))
            # print(tc)
            statusAltPop = float(((int(tc)) / 1024))
            percentAltPop = math.ceil((statusAltPop * 100))
            print("Altitude Generated: ", tc, "Out Of", "1024", "----------", int(percentAltPop), "%")
            t.start()

        # print("Percent Done:", ((altitude_vari / 400 + 0.00001)), "%")

        while A[1023][1023] != -1024:
            time.sleep(1)
            print(
                A[1023][1023])

        valueA.valAlt = A

        # for ix in range(1, nx - 1):
        #     print(A[ix])





