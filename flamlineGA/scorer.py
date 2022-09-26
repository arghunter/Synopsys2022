import numpy as np
from userInfo import *
from genome import *


class Scorer:
    neighborhood = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                    (0, 1), (1, -1), (1, 0), (1, 1))
    EMPTY, TREE, FIRE, BURNT, LINE = 0, 1, 2, 3, 4

    def __init__(self, gnme, X, A):
        self.gnme = gnme
        self.X = np.zeros((sideLength*2+1, sideLength*2+1))
        self.A = A
        self.offsety = (int(ny/2)-sideLength)
        self.offsetx = (int(nx/2)-sideLength)
        self.FIRESX = Queue(maxsize=0)
        self.FIRESY = Queue(maxsize=0)

        for i in range(sideLength*2):
            for j in range(sideLength*2):
                self.X[i, j] = X[i+self.offsety, j+self.offsetx]
                if X[i+self.offsety, j+self.offsetx] == Scorer.FIRE:
                    self.FIRESX.put(j)
                    self.FIRESY.put(i)

    def score(self):
        # print(len(FIRES))
        bs = self.gnme.bx.qsize()
        ts=bs
        count = 0
        offset = seed
        while (self.FIRESX.qsize() > 0):
            np.random.seed(offset)
            offset += 1

            qs = self.FIRESX.qsize()
            if bs > 0:
                for i in range(lineDrawSpeed):
                    if(bs > 0):
                        x = self.gnme.bx.get()
                        y = self.gnme.by.get()
                        bs -= 1
                        if(y-self.offsety>=0 and y-self.offsety<sideLength*2 and x-self.offsetx>=0 and x-self.offsetx<sideLength*2):
                            self.X[y-self.offsety, x-self.offsetx] = Scorer.LINE
                        self.gnme.bx.put(x)
                        self.gnme.by.put(y)

            while (qs > 0):
                qs -= 1
                x1 = int(self.FIRESX.get())
                y1 = int(self.FIRESY.get())
                self.X[y1][x1] = 0

                for dx, dy in Scorer.neighborhood:

                    if int(y1) + dy >= 0 and int(y1) + dy < sideLength*2 and int(x1) + dx >= 0 and int(x1) + dx < sideLength*2 and self.X[
                            int(y1) + dy, int(x1) + dx] == Scorer.TREE and np.random.random() <= spread_chance+(self.A[y1+dy][x1+dx]-self.A[y1][x1])/(1200.0):
                        # print(spread_chance+(A[y1+dy][x1+dx]-A[y1][x1])/(2000))
                        self.X[int(y1) + dy, int(x1) + dx] = Scorer.FIRE
                        count += 1
                        self.FIRESX.put(int(x1) + dx)
                        self.FIRESY.put(int(y1) + dy)
        return count+int(ts/1.2)
