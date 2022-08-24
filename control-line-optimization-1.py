# basic wildfire control line optimization
# Assume that firefighters are able to create a mile of control line every 3 minutes with the help of on-site apparatus.
# This value "flRate" may be changed at anytime by the department


#Draft 1

#Assume fire spreads at 10mph and a tick of 1 second represents an 1 hour and each hexagon represents 10 miles

#20 miles of fire line can be drawn every hour.

from time import sleep

t = 0
while True:
  print(t)
  sleep(1)
  t+=1
 

flRate = 20


