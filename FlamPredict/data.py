import numpy as np
# import pandas as pd

    
geoTIFFPath = ""
square=6000
global F,A,W,C,B,T,p # F Foliage,A Altitude, W Wind speed+direction,C canopy height, B burn dpeed+direction 
if geoTIFFPath=="":
    #Covers a 50kx50km area NOTE: these arrays are stored as y,x coordinates
    
    F=np.zeros((square, square)) # Each cell is 5mx5m 
    print("F")
    F.fill(10)
    A=np.zeros((square, square))
    for y in range(0,square):
        for x in range(0,square):
            A[y,x]=y>>2+x>>2
    print("A")
    W=np.zeros((square, square,2)) # Note wind ninja is typical at resolutions of 100mx100m
    W[0].fill(1)
    W[0].fill(5)
    print("W")
    C=np.zeros((square, square))
    for y in range(0,square):
        for x in range(0,square):
            C[y,x]=A[y,x]+10*np.random.random()
    print("C")
    B=np.zeros((square, square,3)) # each cell i 5mx5m with level 0 = speed level 1 = direction in radians with +x being 0 level 2= time of ignition
    print("B")
    T=0 # Time in seconds since ignition
    p=8
    
            
   