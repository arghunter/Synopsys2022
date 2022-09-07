# basic wildfire control line optimization
# Assume that firefighters are able to create a mile of control line every 3 minutes with the help of on-site apparatus.
# This value "flRate" may be changed at anytime by the department


# Draft 1

# Assume fire spreads at 10mph and a tick of 1 second represents an 1 hour and each hexagon represents 10 miles

# 20 miles of fire line can be drawn every hour.

from time import sleep
import random
# from turtle import down, right
t = 0
s = 25
ground = [None]*s
for x in range(s):
    ground[x] = (random.sample(range(0, 255), s))
for x in range(0, len(ground)):
    print(ground[x])
ground[int(s/2)][int(s/2)] = 1000+ground[int(s/2)][int(s/2)]
while True:
    print(t)
    for x in range(0, s):
        for y in range(0, s):
            if(ground[x][y] < 1000 and ground[x][y] > 0):
                for z in range(1, 4):
                    c = 0
                    left = x >= z and x < s
                    right = x < s-z and x >= 0
                    up = y > z and y < s
                    down = y < s-z and y >= 0
                    if left and ground[x-z][y] >= 1000:
                        c += 1
                    if right and ground[x+z][y] >= 1000:
                        c += 1
                    if up and ground[x][y-z] >= 1000:
                        c += 1
                    if down and ground[x][y+z] >= 1000:
                        c += 1
                    if up and right and ground[x+z][y-z] >= 1000:
                        c += 1
                    if up and left and ground[x-z][y-z] >= 1000:
                        c += 1
                    if down and right and ground[x+z][y+z] >= 1000:
                        c += 1
                    if down and left and ground[x-z][y+z] >= 1000:
                        c += 1

                    if(c*6.25/(2*z) >= random.randint(0, 100) and c != 0):
                        ground[x][y] += 1000
                        break

            else:
                if(ground[x][y] == 1000 or ground[x][y] <= 0):
                    ground[x][y] = 0
                else:
                    ground[x][y] -= 1
#
    for x in range(0, len(ground)):
        print(ground[x])
        # for y in range(0, len(ground[x])):
        #     print(str(ground[x][y])+" ", end="")

    sleep(1)
    t += 1

#move to old
flRate = 20
