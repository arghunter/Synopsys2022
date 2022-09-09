import math

# user information
def userInfo():
    print("----------------------")
    print("a Square is 20m by 20m")
    print("----------------------")

    print()

    fireSpreadSpeed = input("Fire Spread Speed (kmh): ")
    print()
    iFSS = float(fireSpreadSpeed)

    # iFSSC = Number of Ticks in a Minute (because 1 square every tick)
    iFSSC = int((iFSS * 1000) / 20)
    # ms per tick
    tickRATE = (60 / iFSSC) * 1000
    iTR = int(tickRATE)
    print("ms per tick for given Spread Speed: ", iTR)
    print()

    lineDrawSpeed = input("Fireline Draw Speed (kmh): ")
    print()
    iLDS = int(lineDrawSpeed)
    iLDSS = (iLDS * 1000) / 20
    # fireline draw speed in squares per tick = iLDSST
    iLDSST = iLDSS / iFSSC
    print("Fireline Draw Speed in Squares per Tick: ", iLDSST)
    print()

    userDelay = input("Delay time before drawing fireline in # of Ticks: ")
    print()
    iUD = int(userDelay)
    bufferSpace = input("Buffer in # of Squares: ")
    print()
    iBS = int(bufferSpace)

    Tau = ((((4 * iUD) / iLDSST) + ((4 * iBS) / iLDSST) + iBS) / ((1 - (4 / iLDSST))))
    print("original Tau: ", Tau)
    upTau = math.ceil(Tau)
    print("rounded-up Tau: ", upTau)

    # Tau = sidelength value because square = tick
    sideLength = ((upTau + iUD + iBS))

    print("side length: ", sideLength)