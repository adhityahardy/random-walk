import matplotlib.pyplot as plt
import numpy as np
from random import random

#initial position
n_particles = 10
n_iterat = 100

xmin = 0
ymin = 0
xmax = 100
ymax = 100

xrange = xmax - xmin
yrange = ymax - ymin

pos = []
position = []

#initial
for i in range (n_particles):
    xpos = 50
    ypos = 50
    pos.append((xpos,ypos))
position.append(pos)

#iteration random
for i in range(n_iterat):
    updatePos = []
    for j in range(n_particles):
        x = position[i][j][0]
        y = position[i][j][1]
        rand = random()

#right
        if(rand <= 0.25):
            x = x+1
#down
        elif(rand <= 0.50):
            y = y-1
#left
        elif(rand <= 0.75):
            y = y+1
#up
        else:
            y = y + 1

        #perform PBC correction
        if (x > xmax): 
            x = x-xrange
        if (y > ymax):
            y = y-yrange
        if (x < 0): 
            x = x+xrange
        if (y < 0): 
            y = y+yrange
        updatePos.append([x,y])
    position.append(updatePos)

fig, ax = plt.subplots(figsize=(10,10))
for i in range(n_iterat):
  for j in range(n_particles):
    ax.scatter(position[i][j][0], position[i][j][1], s=50, alpha=0.75)

plt.title('Random Walk 2D')
plt.grid()
plt.show()
