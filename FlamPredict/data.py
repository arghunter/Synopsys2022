import numpy as np
# import pandas as pd
class Data:
    
    def __init__(self,geoTIFFPath=""):
        if geoTIFFPath=="":
            #Covers a 50kx50km area NOTE: these arrays are stored as y,x coordinates
            global F,A,W,C,B,T,p # F Foliage,A Altitude, W Wind speed+direction,C canopy height, B burn dpeed+direction 
            F=np.zeros((10000, 10000)) # Each cell is 5mx5m 
            print("F")
            
            A=np.zeros((10000, 10000))
            print("A")
            W=np.zeros((10000, 10000,2)) # Note wind ninja is typical at resolutions of 100mx100m
            print("W")
            C=np.zeros((10000, 10000))
            print("C")
            B=np.zeros((10000, 10000,3)) # each cell i 5mx5m with level 0 = speed level 1 = direction in radians with +x being 0 level 2= time of ignition
            print("B")
            T=0 # Time in seconds since ignition
            p=5
            
            

data=Data()
print(F)
print(A)
print(W)
print(C)
print(B)      