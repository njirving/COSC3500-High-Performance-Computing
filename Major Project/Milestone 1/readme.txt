Instructions for running the code on getafix:

cellular.cpp:
The main program

1. run make - this will compile the .cpp file in 4 modes of optimisation

2. run ./cellular{O level} {size} {ticks} {init file} where "O level" is the level of 
optimisation that you want to run (0, 1, 2, 3), "size" is the row size of the board, 
"ticks" are the number of ticks and "init file" is an optional parameter where you 
can specify a file that has been created by Loader.py for use as an inital state.

    2a. In order to use the optional argument "init file" the size of the board 
    needs to be set to the largest diamension of the orginal image else the program
    will segfault


Viewer.py:
Creates a gif from the output of the main program

1. After running ./cellular there will be an output file of the format data_R=X_T=Y.txt 
where X is the row size of the board and Y is the number of ticks put the directory of 
this file into the FILE variable

2. run python3 Viewer.py

3. To view the animation, open out.gif

An example output gif of a turing machine has been placed in this zip folder (out.gif).
It was done using the provided TuringMachine.bmp processed through Loader.py with a 
board size of 1800 and a tick count of 100, this takes a little time but the reader is 
encouraged to try this image for themselves as well as any other structures they might 
want to draw.


Loader.py:
Processes images in the form of bitmaps into a file that can be read by cellular.cpp

1. Set FILE to the directory of the image

2. Set SAVE_NAME to the desired output directory

3. run python3 Loader.py