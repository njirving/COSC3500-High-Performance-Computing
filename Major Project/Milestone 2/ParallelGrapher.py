import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors
import numpy as np

file_Pnowrite0 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O0_nowrite.out"
file_Pnowrite1 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O1_nowrite.out"
file_Pnowrite2 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O2_nowrite.out"
file_Pnowrite3 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O3_nowrite.out"

file_Snowrite0 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Serial\\results_O0_nowrite.out"
file_Snowrite1 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Serial\\results_O1_nowrite.out"
file_Snowrite2 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Serial\\results_O2_nowrite.out"
file_Snowrite3 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Serial\\results_O3_nowrite.out"

file_P0 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O0.out"
file_P1 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O1.out"
file_P2 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O2.out"
file_P3 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O3.out"

file_S0 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Serial\\results_O0.out"
file_S1 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Serial\\results_O1.out"
file_S2 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Serial\\results_O2.out"
file_S3 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Serial\\results_O3.out"

file_Pnowrite256_0 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O0_nowrite_256.out"
file_Pnowrite256_1 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O0_nowrite_256.out"
file_Pnowrite256_2 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O0_nowrite_256.out"
file_Pnowrite256_3 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O0_nowrite_256.out"

file_Pnowrite512_0 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O0_nowrite_512.out"
file_Pnowrite512_1 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O0_nowrite_512.out"
file_Pnowrite512_2 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O0_nowrite_512.out"
file_Pnowrite512_3 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O0_nowrite_512.out"

file_Pnowrite1024_0 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O0_nowrite_1024.out"
file_Pnowrite1024_1 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O1_nowrite_1024.out"
file_Pnowrite1024_2 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O2_nowrite_1024.out"
file_Pnowrite1024_3 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O3_nowrite_1024.out"

file_P_32_0 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O0_32.out"
file_P_64_0 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O0_64.out"
file_P_128_0 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O0_128.out"
file_P_512_0 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O0_512.out"
file_P_1024_0 = "C:\\Users\\Anymoose\\Documents\\COSC3500\\Major Project\\Data\\Parallel\\results_O0_1024.out"


def file_processor(file):
    f = open(file, 'r')
    rows = []
    time = []
    for l in f:
        s = l.split(' ')
        rows.append(int(s[0].replace("R=", '')))
        time.append(int(s[-1].replace("ms", '')))
    return rows, time

P0rows, P0time = file_processor(file_P0)
P1rows, P1time = file_processor(file_P1)
P2rows, P2time = file_processor(file_P2)
P3rows, P3time = file_processor(file_P3)

S0rows, S0time = file_processor(file_S0)
S1rows, S1time = file_processor(file_S1)
S2rows, S2time = file_processor(file_S2)
S3rows, S3time = file_processor(file_S3)

Pnowriterows0, Pnowritetime0 = file_processor(file_Pnowrite0)
Pnowriterows1, Pnowritetime1 = file_processor(file_Pnowrite1)
Pnowriterows2, Pnowritetime2 = file_processor(file_Pnowrite2)
Pnowriterows3, Pnowritetime3 = file_processor(file_Pnowrite3)

Snowriterows0, Snowritetime0 = file_processor(file_Snowrite0)
Snowriterows1, Snowritetime1 = file_processor(file_Snowrite1)
Snowriterows2, Snowritetime2 = file_processor(file_Snowrite2)
Snowriterows3, Snowritetime3 = file_processor(file_Snowrite3)

Pnowrite256_0_rows, Pnowrite256_0_time = file_processor(file_Pnowrite256_0)
Pnowrite256_1_rows, Pnowrite256_1_time = file_processor(file_Pnowrite256_1)
Pnowrite256_2_rows, Pnowrite256_2_time = file_processor(file_Pnowrite256_2)
Pnowrite256_3_rows, Pnowrite256_3_time = file_processor(file_Pnowrite256_3)

Pnowrite512_0_rows, Pnowrite512_0_time = file_processor(file_Pnowrite512_0)
Pnowrite512_1_rows, Pnowrite512_1_time = file_processor(file_Pnowrite512_1)
Pnowrite512_2_rows, Pnowrite512_2_time = file_processor(file_Pnowrite512_2)
Pnowrite512_3_rows, Pnowrite512_3_time = file_processor(file_Pnowrite512_3)

Pnowrite1024_0_rows, Pnowrite1024_0_time = file_processor(file_Pnowrite1024_0)
Pnowrite1024_1_rows, Pnowrite1024_1_time = file_processor(file_Pnowrite1024_1)
Pnowrite1024_2_rows, Pnowrite1024_2_time = file_processor(file_Pnowrite1024_2)
Pnowrite1024_3_rows, Pnowrite1024_3_time = file_processor(file_Pnowrite1024_3)

P32_0_rows, P32_0_time = file_processor(file_P_32_0)
P64_0_rows, P64_0_time = file_processor(file_P_64_0)
P128_0_rows, P128_0_time = file_processor(file_P_128_0)
P512_0_rows, P512_0_time = file_processor(file_P_512_0)
P1024_0_rows, P1024_0_time = file_processor(file_P_1024_0)



#plt.plot(P0rows, P0time, label = "Parallel O0 flag")
#plt.plot(P1rows, P1time, label = "Parallel O1 flag")
#plt.plot(P2rows, P2time, label = "Parallel O2 flag")
#plt.plot(P3rows, P3time, label = "Parallel O3 flag")

#plt.plot(S0rows, S0time, label = "Serial O0 flag")
#plt.plot(S1rows, S1time, label = "Serial O1 flag")
#plt.plot(S2rows, S2time, label = "Serial O2 flag")
#plt.plot(S3rows, S3time, label = "Serial O3 flag")

#plt.plot(Pnowriterows0, Pnowritetime0, label = "Parallel O0 flag, no disk writes")
#plt.plot(Pnowriterows1, Pnowritetime1, label = "Parallel O1 flag")
#plt.plot(Pnowriterows2, Pnowritetime2, label = "Parallel O2 flag")
#plt.plot(Pnowriterows3, Pnowritetime3, label = "Parallel O3 flag")

#plt.plot(Snowriterows0, Snowritetime0, label = "Serial O0 flag, no disk writes")
#plt.plot(Snowriterows1, Snowritetime1, label = "Serial O1 flag, no disk writes")
#plt.plot(Snowriterows2, Snowritetime2, label = "Serial O2 flag, no disk writes")
#plt.plot(Snowriterows3, Snowritetime3, label = "Serial O3 flag, no disk writes")

#plt.plot(Pnowrite256_0_rows, Pnowrite256_0_time, label = "O0 flag")
#plt.plot(Pnowrite256_1_rows, Pnowrite256_1_time, label = "O1 flag")
#plt.plot(Pnowrite256_2_rows, Pnowrite256_2_time, label = "O2 flag")
#plt.plot(Pnowrite256_3_rows, Pnowrite256_3_time, label = "O3 flag")

#plt.plot(Pnowrite512_0_rows, Pnowrite512_0_time, label = "O0 flag")
#plt.plot(Pnowrite512_1_rows, Pnowrite512_1_time, label = "O1 flag")
#plt.plot(Pnowrite512_2_rows, Pnowrite512_2_time, label = "O2 flag")
#plt.plot(Pnowrite512_3_rows, Pnowrite512_3_time, label = "O3 flag")

#plt.plot(Pnowrite1024_0_rows, Pnowrite1024_0_time, label = "O0 flag")
#plt.plot(Pnowrite1024_1_rows, Pnowrite1024_1_time, label = "O1 flag")
#plt.plot(Pnowrite1024_2_rows, Pnowrite1024_2_time, label = "O2 flag")
#plt.plot(Pnowrite1024_3_rows, Pnowrite1024_3_time, label = "O3 flag")

#plt.plot(P32_0_rows, P32_0_time, label = "O0 flag 32 threads")
#plt.plot(P64_0_rows, P64_0_time, label = "O0 flag 64 threads")
#plt.plot(P128_0_rows, P128_0_time, label = "O0 flag 128 threads")
#plt.plot(P0rows, P0time, label = "O0 flag 256 threads")
#plt.plot(P512_0_rows, P512_0_time, label = "O0 flag 512 threads")
#plt.plot(P1024_0_rows, P1024_0_time, label = "O0 flag 1024 threads")


plt.ylabel("Time (ms)")
plt.xlabel("Board Size")

plt.title("")

plt.legend()
plt.show()