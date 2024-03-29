import numpy as np
from tkinter.tix import Tree
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import math
from matplotlib import animation
from matplotlib import colors




file = open("routput1.txt", 'r')
X = np.loadtxt(file)

# comment back these lines to animate (17 and 20)
fig = plt.figure(figsize=(25 / 3, 6.25))

# Creates 1x1 grid subplot.
ax = fig.add_subplot(111)

# Turns off the x and y axis.
ax.set_axis_off()
colors_list = [(0, 0.4, 0), (0, 0, 1),(1,1,1)]
bounds = [0.0, 1.0]

simulateTime =8000

for i in range(1, simulateTime, 20):
    colors_list.append(((i) / (simulateTime), 0, 0))
    bounds.append(i)
for i in range(simulateTime, 200000):
    colors_list.append((0, 0.4, 0))
    bounds.append(i)
# print(bounds)
cmap = colors.ListedColormap(colors_list)
norm = colors.BoundaryNorm(bounds, cmap.N)

# burnt squares count
flatX = X.flatten()
flatXlen = len(flatX)
# print("flat X len", flatXlen)
burntSq = 0
for i in range(flatXlen):
    if (flatX[i] >2) and (flatX[i] <= simulateTime):
        burntSq += 1

# print("burnt sq #", burntSq)
sqMburnt = burntSq * 900
AcreBurnt = (sqMburnt / 4047)
print("acres burnt at time", simulateTime, "is", AcreBurnt, "acres")
print("squares burnt", burntSq)



def close_event():
   plt.close()  # timer calls this function after 3 seconds and closes the window


# The matplotlib function imshow() creates an image from a 2D numpy array with 1
# square for each array element. X is the data of the image; cmap is a colormap;
# norm maps the data to colormap colors.
im = ax.imshow(X, cmap=cmap, norm=norm)  # , interpolation='nearest')



# The animate function is called to produce a frame for each generation.


# for things that are done every tick, do them here:
def animate(i):
    # animate figure
    im.set_data(animate.X)






   # track number of ticks elapsed







# Binds the grid to the identifier X in the animate function's namespace.
animate.X = X


# Interval between frames (ms).
interval = 200

# animation.FuncAnimation makes an animation by repeatedly calling a function func;
# fig is the figure object used to resize, etc.; animate is the callable function
# called at each frame; interval is the delay between frames (in ms).
# anim = animation.FuncAnimation(fig, animate, interval=interval)
anim = animation.FuncAnimation(fig, animate)





# figure
plt.figure(1)

# contour line levels
# contourLevels = np.arrange(500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000)
contourLevelFrequency = 50


# draw contour
# fig1contour = plt.contour(xAltList, yAltList, A, contourLevelFrequency)

# labels
# plt.clabel(fig1contour, inline=1, fontsize=10)

# scale bar
# plt.colorbar()

#figure title
plt.title('Wildfire Propagation Simulation using Alexandridis Model')

# Display the animated figure

# timer = fig.canvas.new_timer(interval = 3000) #creating a timer object and setting an interval of 3000 milliseconds
# timer.add_callback(close_event)

# timer.start()
plt.show()


