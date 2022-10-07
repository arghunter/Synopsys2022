import numpy as np


# import pandas as pd


geoTIFFPath = ""
square = 6000
global f, a, w, c, b, t, p  # F Foliage,A Altitude, W Wind speed+direction,C canopy height, B burn dpeed+direction
if geoTIFFPath == "":
    # Covers a 50kx50km area NOTE: these arrays are stored as y,x coordinates

    f = np.zeros((square, square))  # Each cell is 5mx5m
    print("F")
    f.fill(10)
    a = np.zeros((square, square))
    for y in range(0, square):
        for x in range(0, square):
            a[y, x] = y >> 2 + x >> 2
    print("A")
    w = np.zeros((square, square, 2))  # Note wind ninja is typical at resolutions of 100mx100m
    w[0].fill(1)
    w[1].fill(5)
    print("W")
    c = np.zeros((square, square))
    # for y in range(0,square):
    #     for x in range(0,square):
    #         C[y,x]=A[y,x]+10*np.random.random()
    print("C")
    b = np.zeros((square, square,
                  4))  # each cell i 5mx5m with level 0 = speed level 1 = direction in radians with +x being 0 level 2= time of ignition level 3 = prob of ignition
    print("B")
    t = 0  # Time in seconds since ignition
    p = 8

