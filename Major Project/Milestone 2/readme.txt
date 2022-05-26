on getafix:

run "make"

run "sbatch slurm.sh"

if you wish to modify the startup parameters go into the slurm script and change the execution to what ever you desire.

Custom initial states can be generated via the Loader.py, just edit a photo in paint, save as a 24 bit bitmap and target the file by modifying the FILE variable in Loader.py. Some examples are provided "TuringMachine" and "testbed".

This output file can be added as a parameter on program startup as the 3rd option example: ./cudaCellular0 80 500 testbed

The output file from the program will have the format "filename_data_R=rows_T=ticks.bin" and can be turned into a gif via ParallelViewer.py by changing the target FILE variable to the desired file name and the "row" variable to the appropriate file. Run this python script and view the output gif. WARNING THIS PROGRAM IS POORLY WRITTEN, FOR USE ONLY AS A TESTING TOOL, TURNING THE OUTPUT INTO A GIF REQUIRES A METRIC TONNE OF RAM, 32 GIGs WAS NOT ENOUGH TO GENERATE A GIF WITH ONLY 200 FRAMES.
