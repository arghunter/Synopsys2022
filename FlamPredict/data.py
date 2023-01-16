import numpy as np

from queue import Queue


# import pandas as pd

class Data:
    neighborhood = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                    (0, 1), (1, -1), (1, 0), (1, 1))

    # global f, a, w, c, b, t, p  # F Foliage,A Altitude, W Wind speed+direction,C canopy height, B burn dpeed+direction
    def __init__(self):
        # geoTIFFPath = input("Enter PATH to LANDFIRE data: ")
        # geoTIFFPath = "C:\\Users\\arg\\Documents\\LandFireData\\T1\\datasmall"
        # geoTIFFPath = "C:/Users/arg/Documents/LandFireData/Mckinney/mckiney"
        # geoTIFFPath = "/Users/Samuel Yuan/Downloads/datasmall/datasmall" #TODO: commentout when done
        # geoTIFFPath = "C:\\Users\\arg\\Documents\\LandFireData\\Mosquito\\mosquito"
        # geoTIFFPath = "/Users/Samuel Yuan/Downloads/mosquito"
        # geoTIFFPath = "C:\\Users\\arg\\Documents\\LandFireData\\Creek\\creek"
        # geoTIFFPath = "/Users/Samuel Yuan/Downloads/mosquito" # mac
        # geoTIFFPath = "/Users/Samuel Yuan/Downloads/mosquito1/mosquito" # winpc
        # geoTIFFPath= "/Users/acg/Downloads/mosquito"
        # geoTIFFPath = "/Users/Samuel Yuan/Downloads/creek (1)/creek" #win pc
        geoTIFFPath="C:\\Users\\arg\\Documents\\LandFireData\\Oak2\\oak2"
        self.spotQ = Queue(maxsize=0)

        # fuel
        fuel = open(geoTIFFPath + "/fuel.asc", "r")
        fuelstring = fuel.readline()
        self.ncols = int(fuelstring[13:len(fuelstring)])
        fuelstring = fuel.readline()
        self.nrows = (int(fuelstring[13:len(fuelstring)]))

        fuelstring = fuel.readline()
        fuelstring = fuel.readline()
        fuelstring = fuel.readline()
        self.p = float(fuelstring[13:len(fuelstring)])
        fuelstring = fuel.readline()
        nodata = fuelstring[14:len(fuelstring)]
        self.fuel = np.loadtxt(fuel)
        for i in range(self.nrows):
            for j in range(self.ncols):
                if self.fuel[i][j] == 98:
                    # print(str(i)+" "+str(j))
                    for dy, dx in Data.neighborhood:
                        if (i + dy < self.nrows and j + dx < self.ncols and i + dy >= 0 and j + dx >= 0 and self.fuel[
                            i + dy, j + dx] != 98):
                            self.fuel[i + dy, j + dx] = 100
        file = open("op.txt", "w");
        for i in range(self.ncols):
            for j in range(self.nrows):
                file.write(str(self.fuel[j][i]) + " ")
            file.write("\n")
        fuel.close()
        print(self.fuel)
        # elevation
        elevation = open(geoTIFFPath + "/elevation.asc", "r")
        elevationstring = elevation.readline()
        self.ncols = int(elevationstring[13:len(elevationstring)])
        elevationstring = elevation.readline()
        self.nrows = (int(elevationstring[13:len(elevationstring)]))

        elevationstring = elevation.readline()
        elevationstring = elevation.readline()
        elevationstring = elevation.readline()
        self.p = float(elevationstring[13:len(elevationstring)])
        elevationstring = elevation.readline()
        nodata = elevationstring[14:len(elevationstring)]
        self.elevation = np.loadtxt(elevation)
        print(self.elevation)
        self.BURN = np.zeros((self.nrows, self.ncols, 3))  # probability,time,direction
        self.COLORS = np.zeros((self.nrows, self.ncols))
        self.FUTURE= np.zeros((self.nrows,self.ncols))
        # atmdir=input("Enter wind directory: ")
        atmdir = geoTIFFPath
        # atmdir = "/Users/Samuel Yuan/Downloads/datasmall/datasmall" #TODO: commentout when done
        # atmname=input("Enter wind atm file name")
        atmname = "elevation_point_07-22-2022_1407_100m.atm"  # TODO: commentout when done

        # atmfileLines = input("Enter number of lines in atm file: ")
        atmfileLines = "348"  # TODO: commentout when done
        self.atmLen = int(atmfileLines) - 2
        atm = open(atmdir + "/" + atmname, "r")
        altFs = atm.readline()
        altFs = atm.readline()
        self.wndV = []
        self.wndA = []
        self.wp = 100
        for i in range(0, self.atmLen):
            altFs = atm.readline()

            fs = altFs.split()
            print(atmdir + "/" + fs[3])
            wndF = open(atmdir + "/" + fs[3], "r")
            wndS = wndF.readline()
            wndS = wndF.readline()
            wndS = wndF.readline()
            wndS = wndF.readline()
            wndS = wndF.readline()
            wndS = wndF.readline()
            wndV = np.loadtxt(wndF)
            print("2")
            wndF = open(atmdir + "/" + fs[4], "r")
            wndS = wndF.readline()
            wndS = wndF.readline()
            wndS = wndF.readline()
            wndS = wndF.readline()
            wndS = wndF.readline()
            wndS = wndF.readline()
            wndA = np.loadtxt(wndF)
            self.wndV.append(wndV)
            self.wndA.append(wndA)
            print(wndV[0].size)
            # print(self.wndV[0].size())

    def get_windV(self, tick, x, y):
        rx = int(x / self.wp)
        ry = int(y / self.wp)
        frame = int(tick / 60)
        if frame >= len(self.wndV):
            frame = len(self.wndV) - 1
        if (rx >= 0 and ry >= 0 and ry < self.nrows and rx < self.ncols):
            return self.wndV[frame][ry][rx] * 1000 / (60 * 60)
        else:
            return -1

    def get_windA(self, tick, x, y):
        rx = int(x / self.wp)
        ry = int(y / self.wp)
        frame = int(tick / 60)
        if frame >= len(self.wndV):
            frame = len(self.wndV) - 1

        if (rx >= 0 and ry >= 0 and ry < self.nrows and rx < self.ncols):
            # print(str(ry)+" "+str(rx)+"\n")
            # print (self.wndA[frame][ry][rx])
            return -(self.wndA[frame][ry][rx] - 270)
        else:
            return -1

    def getLineFuelType(self, ry, rx):
        if int(self.fuel[ry][rx]) in (91, 92, 93, 98, 99, 100):
            # NO FIRE SPREAD
            fuelmodelcode = 0
        elif int(self.fuel[ry][rx]) in (101, 102, 103, 104, 105, 106, 107, 108, 109):
            # Grass
            fuelmodelcode = 1
        elif int(self.fuel[ry][rx]) in (121, 122, 123, 124):
            # brush
            fuelmodelcode = 5
        elif int(self.fuel[ry][rx]) in (141, 142, 143, 144, 145, 146, 147, 148, 149):
            # chapparal
            fuelmodelcode = 4
        elif int(self.fuel[ry][rx]) in (161, 162, 163, 164, 165):
            # open timber with grass understory
            fuelmodelcode = 2
        elif int(self.fuel[ry][rx]) in (181, 182, 183, 184, 185, 186, 187, 188, 189):
            # closed timber litter
            fuelmodelcode = 8
        elif int(self.fuel[ry][rx]) in (201, 202, 203, 204):
            # heavy slash
            fuelmodelcode = 13
        else:
            fuelmodelcode = 0
        return fuelmodelcode

    def getSpeed(self, tick, ry, rx, slope):
        # make sure SLOPE IS GRADE
        bladeWidth = 10  # (ft) from https://www.fire.ca.gov/media/gagbtzop/dozers.pdf
        lineWidth = 40 # (ft)
        fuelmodelcode = self.getLineFuelType(self, ry, rx)
        if fuelmodelcode in (1,2,3,5,8):
            if abs(slope) <= 25:
                if slope >= 0:
                    dozerSpeed = 88
                elif slope < 0:
                    dozerSpeed = 118
            elif 25 < abs(slope) <= 40:
                if slope >= 0:
                    dozerSpeed = 58
                elif slope < 0:
                    dozerSpeed = 112
            elif abs(slope) > 40:
                if slope >= 0:
                    dozerSpeed = 35
                elif slope < 0:
                    dozerSpeed = 73
        elif fuelmodelcode in (4,9,11,12):
            if abs(slope) <= 25:
                if slope >= 0:
                    dozerSpeed = 32
                elif slope < 0:
                    dozerSpeed = 47
            elif 25 < abs(slope) <= 40:
                if slope >= 0:
                    dozerSpeed = 18
                elif slope < 0:
                    dozerSpeed = 53
            elif abs(slope) > 40:
                if slope >= 0:
                    dozerSpeed = 5
                elif slope < 0:
                    dozerSpeed = 31
        elif fuelmodelcode in (6,7):
            if abs(slope) <= 25:
                if slope >= 0:
                    dozerSpeed = 51
                elif slope < 0:
                    dozerSpeed = 75
            elif 25 < abs(slope) <= 40:
                if slope >= 0:
                    dozerSpeed = 26
                elif slope < 0:
                    dozerSpeed = 78
            elif abs(slope) > 40:
                if slope >= 0:
                    dozerSpeed = 9
                elif slope < 0:
                    dozerSpeed = 48
        elif fuelmodelcode in (10,13):
            if abs(slope) <= 25:
                if slope >= 0:
                    dozerSpeed = 17
                elif slope < 0:
                    dozerSpeed = 23
            elif 25 < abs(slope) <= 40:
                if slope >= 0:
                    dozerSpeed = 10
                elif slope < 0:
                    dozerSpeed = 25
            elif abs(slope) > 40:
                if slope >= 0:
                    dozerSpeed = 3
                elif slope < 0:
                    dozerSpeed = 11
        elif fuelmodelcode == 0:
            dozerSpeed = 99999999999999999999

        passesNeeded = lineWidth/bladeWidth
        wdozerSpeed = dozerSpeed/passesNeeded


        if tick < 537:
            n = 1
        elif 537 <= tick < 3500:
            n = 2
        elif tick >= 3500:
            n = 3


        with open('dozerNum.txt', 'r') as dozernumFile:
            dozernumlines = dozernumFile.readlines()

            nthlineD = dozernumlines[(n - 1)]
            dozernumVal = nthlineD.strip()
        dozerNum = float(dozernumVal)

        totaldozerSpeed = dozerNum * wdozerSpeed

        if fuelmodelcode == 1:
            crewSpeed = 18
        elif fuelmodelcode in (2,9):
            crewSpeed = 16
        elif fuelmodelcode in (3,4,13):
            crewSpeed = 3
        elif fuelmodelcode in (5,10,12):
            crewSpeed = 4
        elif fuelmodelcode in (6,8):
            crewSpeed = 5
        elif fuelmodelcode == 7:
            crewSpeed = 2
        elif fuelmodelcode == 11:
            crewSpeed = 9
        elif fuelmodelcode == 0:
            crewSpeed = 99999999999999999999


        with open('crewNum.txt', 'r') as crewnumFile:
            crewnumlines = crewnumFile.readlines()

            nthlineC = crewnumlines[(n - 1)]
            crewnumVal = nthlineC.strip()
        crewNum = float(crewnumVal)

        totalcrewSpeed = crewNum * crewSpeed
        totalSpeedCh = totalcrewSpeed + totaldozerSpeed
        totalSpeed = totalSpeedCh/179 # ch/hr to m/s

        return totalSpeed

    def reset(self):
        self.BURN = np.zeros((self.nrows, self.ncols, 3))  # probability,time,direction
        self.COLORS = np.zeros((self.nrows, self.ncols))
        self.FUTURE= np.zeros((self.nrows,self.ncols))
# data=Data()
# print(data.fuel[10,5]);
# square = 6000
# geoTIFFPath = input("Enter PATH to LANDFIRE data: ")
# data=Data(geoTIFFPath)
# if geoTIFFPath == "":
#     # Covers a 50kx50km area NOTE: these arrays are stored as y,x coordinates

#     f = np.zeros((square, square))  # Each cell is 5mx5m
#     print("F")
#     f.fill(10)
#     a = np.zeros((square, square))
#     for y in range(0, square):
#         for x in range(0, square):
#             a[y, x] = y >> 2 + x >> 2
#     print("A")
#     w = np.zeros((square, square, 2))  # Note wind ninja is typical at resolutions of 100mx100m
#     w[0].fill(1)
#     w[1].fill(5)
#     print("W")
#     c = np.zeros((square, square))
#     # for y in range(0,square):
#     #     for x in range(0,square):
#     #         C[y,x]=A[y,x]+10*np.random.random()
#     print("C")
#     b = np.zeros((square, square,
#                   4))  # each cell i 5mx5m with level 0 = speed level 1 = direction in radians with +x being 0 level 2= time of ignition level 3 = prob of ignition
#     print("B")
#     t = 0  # Time in seconds since ignition
#     p = 8
