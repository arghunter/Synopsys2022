from queue import Queue
import numpy as np
import random
from functools import cmp_to_key

# import files and variables
from data import *


class FireLine:
    # nVe = 4
    # v = np.zeros((nV, 2))  # y,x

    def __init__(self, v, nV):
        # print("yCalled")
        self.nV = nV;
        self.v = v
        self.avgX = 0;
        self.avgY = 0;
        for i in v:
            self.avgX += i[0]
            self.avgY += i[1]
        self.avgX /= self.nV
        self.avgY /= self.nV
        self.forwards = np.random.random() <= 0.5
        self.bx = Queue(maxsize=0)
        self.by = Queue(maxsize=0)
        if self.forwards:
            for i in range(nV):
                self.by.put(int(self.v[i][0]))
                self.bx.put(int(self.v[i][1]))
                cx = int(self.v[i][1])
                cy = int(self.v[i][0])
                t = i + 1
                if (not (i < nV - 1)):
                    t = 0
                # print(str(i)+" "+str(t))
                if (cx == int(self.v[t][1])):
                    slope = 0
                else:
                    slope = (cy - int(self.v[t][0])) / (cx - int(self.v[t][1]))

                if (abs(slope) > 1):
                    lx = cx
                    while (int(cy) != int(self.v[t][0])):
                        d = - \
                            int(abs(cy - int(self.v[t][0])) /
                                (cy - int(self.v[t][0])))
                        # print(str(cx)+" "+str(cy)+" "+str(lx))

                        cx += d / slope
                        if (abs(int(cx) - lx) >= 1):
                            self.bx.put(int(cx))
                            self.by.put(int(cy))
                            lx = int(cx)
                        cy += d

                        self.bx.put(int(cx))
                        self.by.put(int(cy))

                    while (int(cx) != int(self.v[t][1])):
                        d = int((int(self.v[t][1]) - cx) /
                                abs((int(self.v[t][1]) - cx)))
                        cx += d

                        self.bx.put(int(cx))
                        self.by.put(int(cy))
                else:
                    ly = cy
                    while (int(cx) != int(self.v[t][1])):
                        d = - \
                            int(abs(cx - int(self.v[t][1])) /
                                (cx - int(self.v[t][1])))
                        # print(str(cx)+" "+str(cy)+" "+str(ly))
                        cy += slope

                        if abs(ly - int(cy)) >= 1:
                            # print(str(cx)+" "+str(cy)+" "+str(ly)+"2")

                            self.bx.put(int(cx))
                            self.by.put(int(cy))
                            ly = int(cy)
                        cx += d

                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))

                    while (int(cy) != int(self.v[t][0])):
                        d = int((int(self.v[t][0]) - cy) /
                                abs((int(self.v[t][0]) - cy)))
                        cy += d
                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))
        else:
            for i in range(nV):
                self.by.put(int(self.v[nV - 1 - i][0]))
                self.bx.put(int(self.v[nV - 1 - i][1]))
                cx = int(self.v[nV - 1 - i][1])
                cy = int(self.v[nV - 1 - i][0])
                t = nV - 2 - i
                if (t < 0):
                    t = nV - 1
                # print(str(i)+" "+str(t))
                if (cx == int(self.v[t][1])):
                    slope = 0
                else:
                    slope = (cy - int(self.v[t][0])) / (cx - int(self.v[t][1]))

                if (abs(slope) > 1):
                    lx = cx
                    while (int(cy) != int(self.v[t][0])):
                        d = - \
                            int(abs(cy - int(self.v[t][0])) /
                                (cy - int(self.v[t][0])))
                        # print(str(cx)+" "+str(cy)+" "+str(lx))

                        cx += d / slope

                        if (abs(int(cx) - lx) >= 1):
                            # print(str(cx)+" "+str(cy)+" "+str(lx)+"2")
                            self.bx.put(int(cx))
                            self.by.put(int(cy))
                            lx = int(cx)
                        cy += d
                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))

                    while (int(cx) != int(self.v[t][1])):
                        d = int((int(self.v[t][1]) - cx) /
                                abs((int(self.v[t][1]) - cx)))
                        cx += d
                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))
                else:
                    ly = cy
                    while (int(cx) != int(self.v[t][1])):
                        d = - \
                            int(abs(cx - int(self.v[t][1])) /
                                (cx - int(self.v[t][1])))
                        # print(str(cx)+" "+str(cy)+" "+str(ly))

                        cy += slope
                        if abs(ly - int(cy)) >= 1:
                            # print(str(cx)+" "+str(cy)+" "+str(ly)+"2")
                            self.bx.put(int(cx))
                            self.by.put(int(cy))
                            ly = int(cy)
                        cx += d
                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))

                    while (int(cy) != int(self.v[t][0])):
                        d = int((int(self.v[t][0]) - cy) /
                                abs((int(self.v[t][0]) - cy)))
                        cy += d
                        # print(str(cx)+" "+str(cy)+" " +
                        #       str(int(self.v[t][1]))+" "+str(int(self.v[t][0])))
                        self.bx.put(int(cx))
                        self.by.put(int(cy))

    def floodFill(self, data, X, rx, ry, sms):

        q = Queue(0)
        q.put((rx, ry))
        size = 0

        while (not q.empty()):
            p = q.get()
            rx = p[0]
            ry = p[1]

            if not (not (rx >= 0 and ry >= 0 and ry < data.nrows and rx < data.ncols) or data.X[ry][rx] != 0):
                size += 1
                # print(str(data.COLORS[ry][rx])+" "+ str(ry)+" "+str(rx)+" "+str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2))
                X[ry][rx] = 1
                q.put((rx + 1, ry))
                q.put((rx - 1, ry))
                q.put((rx, ry + 1))
                q.put((rx, ry + 1))
                q.put((rx + 1, ry + 1))
                q.put((rx + 1, ry - 1))
                q.put((rx - 1, ry - 1))
                q.put((rx - 1, ry + 1))
        return size

    def execute(self, data):
        print("Execuring")
        qs = self.bx.qsize();
        while (qs > 0):
            qs -= 1
            ry = self.by.get()
            rx = self.bx.get()
            # print("Executing"+ str(rx)+" "+str(ry))
            if (ry < data.nrows and rx < data.ncols and ry >= 0 and rx >= 0):
                data.BURN[ry][rx][1] = 1;

    def getScore(self, data, buffer, time, speedms, X):
        qs = self.bx.qsize()
        scoreW = 1000;
        while (qs > 0):
            rx = self.bx.get();
            ry = self.by.get();
            if (ry < data.nrows and rx < data.ncols and ry >= 0 and rx >= 0):
                X[ry][rx] = -1;
            self.bx.put(rx)
            self.by.put(ry)
        score = self.floodFill(data, X, int(self.avgX), int(self.avgY))

        lx = self.bx.get();
        ly = self.by.get();
        for i in range(6):
            for j in range(6):
                if (ly - 3 + i >= 0 and ly - 3 + i < data.nrows and lx - 3 + j >= 0 and lx - 3 + j < data.ncols):
                    if (data.BURN[ly - 3 + i][lx - 3 + j] < time + buffer and not (X[ly - 3 + i][lx - 3 + j] == 2)):
                        score += scoreW
                        X[ly - 3 + i][lx - 3 + j] = 2

        while (not self.bx.empty()):
            rx = self.bx.get();
            ry = self.by.get();
            dy = ry - ly;
            dx = rx - lx;
            d = np.sqrt(dy ** 2 + dx ** 2)
            time += d / speedms
            ly = ry
            lx = rx
            for i in range(6):
                for j in range(6):
                    if (ly - 3 + i >= 0 and ly - 3 + i < data.nrows and lx - 3 + j >= 0 and lx - 3 + j < data.ncols):
                        if (data.BURN[ly - 3 + i][lx - 3 + j] < time + buffer and not (X[ly - 3 + i][lx - 3 + j] == 2)):
                            score += scoreW
                            X[ly - 3 + i][lx - 3 + j] = 2
        return score


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.y2 = y2
        self.x2 = x2

    def intersects(self, other):
        return ((self.x1 <= other.x1 and self.x2 >= other.x1 or other.x1 <= self.x1 and other.x2 >= self.x1) and (
                    self.y1 <= other.y1 and self.y2 >= other.y1 or other.y1 <= self.y1 and other.y2 >= self.y1))


def dir(bp, p1, p2):
    det = (p1[1] - bp[1]) * (p2[0] - p1[0]) - (p1[0] - bp[0]) * (p2[1] - p1[1])
    if det == 0:
        return 0
    elif det > 0:
        return 1;
    else:
        return 2;


def eulerdist2(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


class Genome:
    def __init__(self, points):
        self.bp = (0, 0)
        vert = self.convexHull(points)
        print(vert)
        self.lines = [FireLine(vert, len(vert))]

    def cmp(self, a, b):
        # return a[0]<b[0];
        dr = dir(self.bp, a, b)
        if dr == 0:
            if (eulerdist2(self.bp, b) >= eulerdist2(self.bp, a)):
                return -1;
            else:
                return 1;
        else:
            if dr == 2:
                return -1
            else:
                return 1

    def convexHull(self, points):
        minv = points[0][1]
        min = 0
        for i in range(1, len(points)):
            if (points[i][1] < minv or points[i][1] == minv and points[i][0] < points[min][0]):
                minv = points[i][1]
                min = i
        points[0], points[min] = points[min], points[0]
        self.bp = points[0];
        nl = 1
        points = sorted(points, key=cmp_to_key(self.cmp))
        for i in range(1, len(points)):
            while ((i < len(points) - 1)) and (dir(self.bp, points[i], points[1]) == 0):
                i += 1
            points[nl] = points[i]
            nl += 1
        if nl < 3:
            return
        vert = [points[0], points[1], points[2]]
        for i in range(3, nl):
            while (len(vert) > 1) and (dir(vert[-2], vert[-1], points[i]) != 2):
                vert.pop()
            vert.append(points[i])
        return vert

    def execute(self, data):
        print("exuriutingngjdsh")
        for line in self.lines:
            print("Here")
            line.execute(data)

    def floodFill(self, data, X, simtime):

        q = Queue(0)
        q.put((rx, ry))

        score = 0
        while (not q.empty()):
            p = q.get()
            rx = p[0]
            ry = p[1]

            if not (not (rx >= 0 and ry >= 0 and ry < data.nrows and rx < data.ncols) or X[ry][rx] == 0):

                if (data.BURN[ry][rx] > 0 and data.BURN[ry][rx] <= simtime):
                    score += 1000

                # print(str(data.COLORS[ry][rx])+" "+ str(ry)+" "+str(rx)+" "+str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2))
                X[ry][rx] = 1
                q.put((rx + 1, ry))
                q.put((rx - 1, ry))
                q.put((rx, ry + 1))
                q.put((rx, ry + 1))
                q.put((rx + 1, ry + 1))
                q.put((rx + 1, ry - 1))
                q.put((rx - 1, ry - 1))
                q.put((rx - 1, ry + 1))

    def getFitness(self, data, buffer, time, speedms):
        score = 0;
        X = np.zeros(data.COLORS.shape())

        for l in self.lines:
            score += l.getScore(data, buffer, time, speedms)
        for i in data.ncols:
            for j in data.nrows:
                score += self.floodFill(data, X, i, j)














