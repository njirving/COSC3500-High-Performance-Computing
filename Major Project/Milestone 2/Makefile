CXX?=g++
CXXFLAGS?=-std=c++11 -g

NVCC?=nvcc
NVFLAGS?=-g --gpu-architecture=sm_35 -Wno-deprecated-gpu-targets

TARGETS=cudaCellular

default : all


all : 
	$(NVCC) -std=c++11 $(NVFLAGS) -Xptxas -O0 -o cudaCellular0 cellular.cu
	$(NVCC) -std=c++11 $(NVFLAGS) -Xptxas -O1 -o cudaCellular1 cellular.cu
	$(NVCC) -std=c++11 $(NVFLAGS) -Xptxas -O2 -o cudaCellular2 cellular.cu
	$(NVCC) -std=c++11 $(NVFLAGS) -Xptxas -O3 -o cudaCellular3 cellular.cu

clean:
	rm -f $(TARGETS) *.o

.PHONY: clean default all