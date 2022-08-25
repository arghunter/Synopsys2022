#note: line = LINE
# The NumPy library is used to generate random numbers in the model.
import numpy as np

# The Matplotlib library is used to visualize the forest fire animation.
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import colors

# A given cell has 8 neighbors: 1 above, 1 below, 1 to the left, 1 to the right, 
# and 4 diagonally. The 8 sets of parentheses correspond to the locations of the 8 
# neighboring cells.
neighborhood = ((-1,-1), (-1,0), (-1,1), (0,-1), (0, 1), (1,-1), (1,0), (1,1))

# Assigns value 0 to EMPTY, 1 to TREE, and 2 to FIRE, 3 to LINE. Each cell in the grid is 
# assigned one of these values.
#add fireline as LINE
EMPTY, TREE, FIRE, LINE = 0, 1, 2, 3


# colors_list contains colors used in the visualization: brown for EMPTY, 
# dark green for TREE, and orange for FIRE. Note that the list must be 1 larger 
# than the number of different values in the array. Also note that the 4th entry 
# (‘orange’) dictates the color of the fire.
colors_list = [(0.2,0,0), (0,0.5,0), (1,0,0), 'orange', 'white']
cmap = colors.ListedColormap(colors_list)


# The bounds list must also be one larger than the number of different values in 
# the grid array.
bounds = [0,1,2,3,4]


# Maps the colors in colors_list to bins defined by bounds; data within a bin 
# is mapped to the color with the same index.
norm = colors.BoundaryNorm(bounds, cmap.N)

# The function firerules iterates the forest fire model according to the 4 model 
# rules outlined in the text.
def firerules(X):

    # X1 is the future state of the forest; ny and nx (defined as 100 later in the 
    # code) represeent the number of cells in the x and y directions, so X1 is an 
    # array of 0s with 100 rows and 100 columns).
    # RULE 1 OF THE MODEL is handled by setting X1 to 0 initially and having no 
    # rules that update FIRE cells. 
    X1 = np.zeros((ny, nx))    
	# For all indices on the grid excluding the border region (which is always empty). 
    	# Note that Python is 0-indexed.
	for ix in range(1,nx-1):         
		for iy in range(1,ny-1):    
			# THIS CORRESPONDS TO RULE 4 OF THE MODEL. If the current value at 
            		# the index is 0 (EMPTY), roll the dice (np.random.random()); if the 
            		# output float value <= p (the probability of a tree being growing), 
            		# the future value at the index becomes 1 (i.e., the cell transitions 
            		# from EMPTY to TREE).
			if X[iy,ix] == LINE:                 
				X1[iy,ix] = LINE            
			if X[iy,ix] == EMPTY and np.random.random() <= p:                 
				X1[iy,ix] = TREE            
			# THIS CORRESPONDS TO RULE 2 OF THE MODEL.
            		# If any of the 8 neighbors of a cell are burning (FIRE), the cell 
            		# (currently TREE) becomes FIRE.
			if X[iy,ix] == TREE:                 
				X1[iy,ix] = TREE        
				# To examine neighbors for fire, assign dx and dy to the 
               	  		# indices that make up the coordinates in neighborhood. E.g., for 
                 		# the 2nd coordinate in neighborhood (-1, 0), dx is -1 and dy is 0. 

				for dx,dy in neighborhood:                     
					if X[iy+dy,ix+dx] == FIRE:                         
						X1[iy,ix] = FIRE                         
						break    
				# THIS CORRESPONDS TO RULE 3 OF THE MODEL.
                	 	# If no neighbors are burning, roll the dice (np.random.random()); 
                 		# if the output float is <= f (the probability of a lightning 
                 		# strike), the cell becomes FIRE.
				#else:                     
				#	if np.random.random() <= f:                         
				# 	X1[iy,ix] = FIRE
				#initial fire
				else:                     
					if np.random.random() <= f:                         
						X1[50,50] = FIRE    
         return X1
    


# The initial fraction of the forest occupied by trees.
forest_fraction = 0.2

# p is the probability of a tree growing in an empty cell; f is the probability of 
# a lightning strike.
p, f = 0.05, 0.001

# Forest size (number of cells in x and y directions).
nx, ny = 100, 100

# Initialize the forest grid. X can be thought of as the current state. Make X an 
# array of 0s.
X = np.zeros((ny, nx))

# X[1:ny-1, 1:nx-1] grabs the subset of X from indices 1-99 EXCLUDING 99. Since 0 is 
# the index, this excludes 2 rows and 2 columns (the border). 
# np.random.randint(0, 2, size=(ny-2, nx-2)) randomly assigns all non-border cells 
# 0 or 1 (2, the upper limit, is excluded). Since the border (2 rows and 2 columns) 
# is excluded, size=(ny-2, nx-2).
X[1:ny-1, 1:nx-1] = np.random.randint(0, 2, size=(ny-2, nx-2))

# This ensures that the number of 1s in the array is below the threshold established 
# by forest_fraction. Note that random.random normally returns floats between 
# 0 and 1, but this was initialized with integers in the previous line of code.
X[1:ny-1, 1:nx-1] = np.random.random(size=(ny-2, nx-2)) < forest_fraction


#line bounds
X[0:5, 0:100] = LINE
X[5:10, 0:30] = LINE
X[5:10, 70:100] = LINE
X[10:80, 0:20] = LINE
X[10:80, 80:100] = LINE
X[80:90, 0:30] = LINE
X[80:90, 70:100] = LINE
X[90:100, 0:100] = LINE

# Adjusts the size of the figure.
fig = plt.figure(figsize=(25/3, 6.25))

# Creates 1x1 grid subplot.
ax = fig.add_subplot(111)

# Turns off the x and y axis.
ax.set_axis_off()

# The matplotlib function imshow() creates an image from a 2D numpy array with 1 
# square for each array element. X is the data of the image; cmap is a colormap; 
# norm maps the data to colormap colors.
im = ax.imshow(X, cmap=cmap, norm=norm) #, interpolation='nearest')

# The animate function is called to produce a frame for each generation.
def animate(i):
     im.set_data(animate.X)
     animate.X = firerules(animate.X)

# Binds the grid to the identifier X in the animate function's namespace.
animate.X = X

# Interval between frames (ms).
interval = 100

# animation.FuncAnimation makes an animation by repeatedly calling a function func;
# fig is the figure object used to resize, etc.; animate is the callable function 
# called at each frame; interval is the delay between frames (in ms).
anim = animation.FuncAnimation(fig, animate, interval=interval)

# Display the animated figure
plt.show()
