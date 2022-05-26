from PIL import Image
import numpy as np

FILE = "TuringMachine.bmp"
SAVE_NAME = "output"

img= Image.open(FILE)
img = np.array(img)  
binarr = np.where(img>128, 0, 1)

outarr = []

for j in range(len(binarr)):
    if len(outarr) < j + 1:
        outarr.append([])
    for i in range(len(binarr[j])):
        outarr[j].append(binarr[j][i][0])

np.savetxt(SAVE_NAME, outarr, fmt='%d', delimiter='')