import numpy as np


# import pandas as pd
class Data:
    # global f, a, w, c, b, t, p  # F Foliage,A Altitude, W Wind speed+direction,C canopy height, B burn dpeed+direction
    def __init__(self):
        # geoTIFFPath = input("Enter PATH to LANDFIRE data: ")
        # geoTIFFPath = "C:\\Users\\arg\\Documents\\LandFireData\\T1\\datasmall"
        # geoTIFFPath = "C:/Users/arg/Documents/LandFireData/Mckinney/mckiney"
        # geoTIFFPath = "/Users/Samuel Yuan/Downloads/datasmall/datasmall" #TODO: commentout when done
        geoTIFFPath = "C:\\Users\\arg\\Documents\\LandFireData\\Mosquito\\mosquito"
        # geoTIFFPath = "/Users/Samuel Yuan/Downloads/mosquito"

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
        # atmdir=input("Enter wind directory: ")
        atmdir = geoTIFFPath
        # atmdir = "/Users/Samuel Yuan/Downloads/datasmall/datasmall" #TODO: commentout when done
        # atmname=input("Enter wind atm file name")
        atmname = "elevation_point_09-06-2022_1736_100m.atm"  # TODO: commentout when done

        # atmfileLines = input("Enter number of lines in atm file: ")
        atmfileLines = "75"  # TODO: commentout when done
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
            return 360-(self.wndA[frame][ry][rx] - 270)
        else:
            return -1

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
