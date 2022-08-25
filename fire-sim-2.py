from math import*
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib as mpl
#création de la forêt
'''0=humus ; 1=arbre vivant ; 3=flammes ; 2=cendres'''

#definition des paramètres
a=400         #hauteur de l'image en nb de pixels
b=400      #largeur de l'image
density=0.65   #densité de la forêt
i=200          #ordonnée du départ du feu
j=300       #abscisse du départ du feu
p=0.5          #percolation
v=100
w=100

def creerforet(n,p,d):  
    D=[]
    k=0
    while k<1000:
        if k<d*1000:
            D.append(1)
            k+=1
        else:
            D.append(0)
            k+=1
        
    forest=np.zeros((n,p))
    for y in range(n):
        for x in range(p):
            forest[y,x]=D[random.randint(0,999)]
    return forest
    
    
foret=creerforet(a,b,density)

foret[i,j]=3
#foret[v,w]=3

fig = plt.figure(figsize=(15,15))


def step(): 
    Feu=[]  #liste contenant toutes les coordonnees des arbres en train de bruler
    for y in range(a):
        for z in range(b):
            if foret[y][z]==3:
                Feu.append([y,z])
    Perc=[]
    l=0
    while l<1000:
        if l<p*1000:
            Perc.append(3)
            l+=1
        else:
            Perc.append(1)
            l+=1
    for x in range(len(Feu)):
        r=Feu[x][0]
        s=Feu[x][1]

        if foret[r+1,s]==1:
            foret[r+1,s]=Perc[random.randint(0,999)]
        if foret[r+1,s-1]==1:
            foret[r+1,s-1]=Perc[random.randint(0,999)]
        if foret[r+1,s+1]==1:
            foret[r+1,s+1]=Perc[random.randint(0,999)]

        if foret[r-1,s-1]==1:
            foret[r-1,s-1]=Perc[random.randint(0,999)]
        if foret[r-1,s]==1:
            foret[r-1,s]=Perc[random.randint(0,999)]
        if foret[r-1,s-1]==1:
            foret[r-1,s-1]=Perc[random.randint(0,999)]

        if foret[r,s+1]==1:
            foret[r,s+1]=Perc[random.randint(0,999)]
        if foret[r,s-1]==1:
            foret[r,s-1]=Perc[random.randint(0,999)]

    #reduction en cendres des arbres brulés à l'étape précédente        
    for y in range(len(Feu)):
        foret[Feu[y][0]][Feu[y][1]]=2
    return foret
        
CM = mpl.colors.ListedColormap([[0.29,0.01,0,0.6],[0.156,0.59,0,1],[0.1,0.1,0.1,1], [0.87,0.3,0.2,0.9]])
im = plt.imshow(step(), cmap=CM, interpolation='none')


 
def updatefig(*args):
    im.set_array(step())
    return im,
 
 

ani = animation.FuncAnimation(fig, updatefig, interval=10, blit=True)
# anim.save can be called in a few different ways, some which might or might not work
# on different platforms and with different versions of matplotlib and video encoders
#anim.save('animation.mp4', fps=20, extra_args=['-vcodec', 'libx264'], writer=animation.FFMpegWriter())
#anim.save('animation.mp4', fps=20, extra_args=['-vcodec', 'libx264'])
#anim.save('animation.mp4', fps=20, writer="ffmpeg", codec="libx264")
#anim.save('animation.mp4', fps=20, writer="avconv", codec="libx264")
plt.axis('off')
plt.show()
