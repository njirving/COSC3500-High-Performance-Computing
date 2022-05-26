import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors
import numpy as np

FILE = "testbed_data_R=80_T=500.bin"

row = 80

size = row**2
data = []
tick = 0
heck = -1
f = open(FILE, 'rb')

byte = f.read()

iterations = 0

for b in byte:
    data.append(int(b))

data = np.array_split(data, len(data)/size)

for i in range(0, len(data)):
    data[i] = np.array_split(data[i], row)

cmap = colors.ListedColormap(['black'])
cmap.set_bad(color='w', alpha=0)

fig = plt.figure()

im = plt.imshow(data[0], cmap='Greys', interpolation='nearest', animated=True)

#plt.axis('off')
#plt.show()

def update(*args):
    global heck

    if len(data)-1 > heck:
        heck += 1

    im.set_array(data[heck])

    return im

anim = animation.FuncAnimation(fig, update, frames=len(data), interval=100)
anim.save("out.gif", dpi=200)