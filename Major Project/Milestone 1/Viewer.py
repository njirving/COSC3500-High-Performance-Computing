import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors
import numpy as np

FILE = "data.txt"

fp = open(FILE)

data = []
rowSize = 0
tick = 0
heck = -1

for line in fp:
    rowSize = int(line[:-1])
    break

for line in fp:
    iterations = 0
    data.append([])
    for c in line:
        if c != '\n' and not c > '1':
            data[tick].append(float(c))
    tick += 1

for i in range(0, len(data)):
    data[i] = np.array_split(data[i], rowSize)

cmap = colors.ListedColormap(['black'])
cmap.set_bad(color='w', alpha=0)

fig = plt.figure()

im = plt.imshow(data[heck], cmap='Greys', interpolation='nearest', animated=True)
plt.axis('off')

def update(*args):
    global heck
    if len(data)-1 > heck:
        heck += 1
    im.set_array(data[heck])
    return im

anim = animation.FuncAnimation(fig, update, frames=len(data)-1, interval=100)
anim.save("out.gif", dpi=750)

#plt.show()