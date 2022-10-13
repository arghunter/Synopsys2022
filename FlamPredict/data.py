import numpy as np


# import pandas as pd
class Data:
    # global f, a, w, c, b, t, p  # F Foliage,A Altitude, W Wind speed+direction,C canopy height, B burn dpeed+direction
    def __init__ (self):
        geoTIFFPath = input("Enter PATH to LANDFIRE data: ")
    # geoTIFFPath = input("Enter PATH to LANDFIRE data: ")
        #fuel
        fuel = open(geoTIFFPath+"/fuel.asc", "r")
        fuelstring=fuel.readline()
        self.ncols=int(fuelstring[13:len(fuelstring)])
        fuelstring=fuel.readline()
        self.nrows=(int(fuelstring[13:len(fuelstring)]))
        
        fuelstring=fuel.readline()
        fuelstring=fuel.readline()
        fuelstring=fuel.readline()
        self.p= float(fuelstring[13:len(fuelstring)])
        fuelstring=fuel.readline()
        nodata=fuelstring[14:len(fuelstring)]
        self.fuel=np.loadtxt(fuel)
        fuel.close()
        print(self.fuel)
        #elevation
        elevation = open(geoTIFFPath+"/elevation.asc", "r")
        elevationstring=elevation.readline()
        self.ncols=int(elevationstring[13:len(elevationstring)])
        elevationstring=elevation.readline()
        self.nrows=(int(elevationstring[13:len(elevationstring)]))
        
        elevationstring=elevation.readline()
        elevationstring=elevation.readline()
        elevationstring=elevation.readline()
        self.p= float(elevationstring[13:len(elevationstring)])
        elevationstring=elevation.readline()
        nodata=elevationstring[14:len(elevationstring)]
        self.elevation=np.loadtxt(elevation)
        print(self.elevation)
        self.BURN=np.zeros((self.nrows,self.ncols,3))#probability,time,direction
        atmdir=input("Enter wind directory: ")
        atmname=input("Enter wind atm file name")
        self.atmLen=int(input("Enter number of lines in atm file: "))-2
        atm= open(atmdir+"/"+atmname,"r")
        altFs=atm.readline()
        altFs=atm.readline()
        self.wndV=[]
        self.wndA=[]
        for i in range(0,self.atmLen):
            altFs=atm.readline()
        
            fs=altFs.split()
            print(atmdir+"/"+fs[3])
            wndF=open(atmdir+"/"+fs[3],"r")
            wndS=wndF.readline()
            wndS=wndF.readline()
            wndS=wndF.readline()
            wndS=wndF.readline()
            wndS=wndF.readline()
            wndS=wndF.readline()
            wndV=np.loadtxt(wndF)
            print("2")
            wndF=open(atmdir+"/"+fs[4],"r")
            wndS=wndF.readline()
            wndS=wndF.readline()
            wndS=wndF.readline()
            wndS=wndF.readline()
            wndS=wndF.readline()
            wndS=wndF.readline()
            wndA=np.loadtxt(wndF)
            self.wndV.append(wndV)
            self.wndA.append(wndA)
            print(wndV)
            print(wndA)
            
            
            
        
    def get_windV(self,tick,x,y):
        rx=int(x/100)
        ry=int(y/100)
        frame=int(tick/60)
        if frame>len(self.wndV):
            frame=len(self.wndV)-1
        return self.wndV[frame][ry][rx]
           
    def get_windA(self,tick,x,y):
        rx=int(x/100)
        ry=int(y/100)
        frame=int(tick/60)
        if frame>len(self.wndV):
            frame=len(self.wndV)-1
        return self.wndA[frame][ry][rx]*np.pi/180
        
        

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

