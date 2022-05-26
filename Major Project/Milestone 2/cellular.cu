#include <iostream>
#include <cstdlib>
#include <vector>
#include <iterator>
#include <fstream>
#include <chrono>
#include <string>
#include <iostream>
#include <stdio.h>
#include <cstring>

#define MAX_BUFFER_BYTES 400000000

using namespace std;

/**
*   Prints the current state, used for debugging
*
*/
void print_state(int* state, int rowSize) 
{
    for (auto i = 0; i < rowSize*rowSize; i++) {
        if (i % rowSize == 0) {
            std::cerr << "\n";
        }
        if (state[i] == 0) {
            std::cerr << ".";
        } else {
            std::cerr << "x";
        }
    }
    std::cerr << "\n";
}

/**
*   Initial state is read from a file and put into the state array
*
*/

void init_from_file(std::string name, int* state, int rowSize) 
{
    std::ifstream file;
    file.open(name);
    int i, j = 0;
    std::string line;
    std::getline (file, line);
    while (!file.eof()) {
        for (char c : line) {
            state[i + j * rowSize] = c - '0';
            i++;
        }
        j++;
        i = 0;
        std::getline (file, line);
    }
}

/**
*   Streams binary data to a file
*
*/
void stream_to_file(int rowSize, std::string filename, int* state, int bufftimes)
{
    std::ofstream outFile;
    int size = rowSize*rowSize*bufftimes;
    outFile.open(filename.c_str(), ios::binary | ios::app);

    for (int i = 0; i < size; i++) {
        outFile.write((char*) (&state[i]), 1);
    }

    outFile.flush();
    outFile.close();
}

/**
*   Adds state to state buffer
*
*/
void add_to_buffer(int* state, int* buffer, int rowSize, int bufftimes) 
{
    int size = rowSize*rowSize*bufftimes;
    std::memcpy(&buffer[size], state, rowSize*rowSize*sizeof(int));
}

/**
*   Prints the CUDA error to the stderr stream, shamlessly stolen from the tutorials
*
*/
void checkError(cudaError_t e)
{
   if (e != cudaSuccess) {
      std::cerr << "CUDA error: " << int(e) << " : " << cudaGetErrorString(e) << '\n';
      abort();
   }
}

/**
*   num_numbers transferred from the serial implementation to a device function that can
*   be run on the GPU.
*
*/
__device__ int num_neighbours(int x, int y, int rowSize, int* state) 
{
    int num = 0;
    
    int xm1 = x - 1;
    int ym1 = y - 1;
    int xp1 = x + 1;
    int yp1 = y + 1;

    if (x == 0) {
        xm1 = rowSize - 1;
    }
    if (x == rowSize - 1) {
        xp1 = 0;
    }
    if (y == 0) {
        ym1 = rowSize - 1;
    }
    if (y == rowSize - 1) {
        yp1 = 0;
    }

    num += state[xm1 + y*rowSize] 
    + state[xp1 + y*rowSize] 
    + state[x + ym1*rowSize]
    + state[x + yp1*rowSize]
    + state[xm1 + ym1*rowSize]
    + state[xp1 + yp1*rowSize]
    + state[xm1 + yp1*rowSize]
    + state[xp1 + ym1*rowSize];

    return num;
}

/**
*   CUDA kernal, handles each cell each tick
*
*/
__global__ void tick(int* state, int* savedState, int rowSize) 
{
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    int x = i % rowSize;
    int y = i / rowSize;
    int num = num_neighbours(x, y, rowSize, state);
    int cell = state[x + y * rowSize];

    savedState[i] = ((num == 3 || num == 2) && cell == 1) || (num == 3 && cell == 0);
}


int main(int argc, char** argv)
{
    if (argc < 3) {
        std::cerr << "Usage: ./cudaCellular {size} {ticks} {file name}" << std::endl;
        exit(0);
    }

    //Init variables
    int rowSize = std::stoi(argv[1]);
    int ticks = std::stoi(argv[2]);
    int* deviceState;
    int* deviceSavedState;
    int* state = (int*)calloc(rowSize * rowSize, sizeof(int)); 
    int* savedState = (int*)calloc(rowSize * rowSize, sizeof(int)); 
    std::string fileName;

    int maxCopies = MAX_BUFFER_BYTES/(rowSize* rowSize);

    cerr << maxCopies << "\n";

    int* buffer = (int*)calloc(rowSize*rowSize*(maxCopies+1), sizeof(int));
    
    if (argc == 4) {
        init_from_file(argv[3], state, rowSize);
        fileName = std::string(argv[3]) + "_data_R=" + std::to_string(rowSize) + "_T=" + std::to_string(ticks) + ".bin";
    } else {
        std::srand(4);
        for (int i = 0; i < rowSize * rowSize; i++) {
            state[i] = std::rand() % 2;
        }
        fileName = "data_R=" + std::to_string(rowSize) + "_T=" + std::to_string(ticks) + ".bin";
    }

    //Removing any files with the same name as the .bin file so we don't append to random data
    remove(fileName.c_str());

    //Allocate memory on the device
    checkError(cudaMalloc(&deviceState, rowSize*rowSize*sizeof(double)));
    checkError(cudaMalloc(&deviceSavedState, rowSize*rowSize*sizeof(double)));

    //Copy states over to the device
    checkError(cudaMemcpy(deviceState, state, rowSize*rowSize*sizeof(int), cudaMemcpyHostToDevice));
    checkError(cudaMemcpy(deviceSavedState, savedState, rowSize*rowSize*sizeof(int), cudaMemcpyHostToDevice));

    int Threads = 256;
    int Blocks = (rowSize*rowSize + Threads - 1)/Threads;

    //Init clock
    auto start = std::chrono::high_resolution_clock::now();

    int bufftimes = 1;

    /*
    *   Main loop
    */
    for (int i = 0; i < ticks; i++) {

        add_to_buffer(state, buffer, rowSize, bufftimes);
        bufftimes++;

        if (i != 0 && (i + 1) % maxCopies == 0) {
            stream_to_file(rowSize, fileName, buffer, bufftimes);
            bufftimes = 0;
        }

        tick<<<Blocks, Threads>>>(deviceState, deviceSavedState, rowSize);
        checkError(cudaDeviceSynchronize());

        checkError(cudaMemcpy(state, deviceState, rowSize*rowSize*sizeof(int), cudaMemcpyDeviceToHost));
        checkError(cudaMemcpy(savedState, deviceSavedState, rowSize*rowSize*sizeof(int), cudaMemcpyDeviceToHost));

        std::swap(state, savedState);

        checkError(cudaMemcpy(deviceState, state, rowSize*rowSize*sizeof(int), cudaMemcpyHostToDevice));
        checkError(cudaMemcpy(deviceSavedState, savedState, rowSize*rowSize*sizeof(int), cudaMemcpyHostToDevice));
    }

    checkError(cudaMemcpy(state, deviceState, rowSize*rowSize*sizeof(int), cudaMemcpyDeviceToHost));
    checkError(cudaMemcpy(savedState, deviceSavedState, rowSize*rowSize*sizeof(int), cudaMemcpyDeviceToHost));
    
    stream_to_file(rowSize, fileName, buffer, bufftimes);

    //Stop clock and get diff, print diff to the stdout stream
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
    std::cout << "R=" << argv[1] << " T=" << argv[2] << " " << duration << "ms" << std::endl;

    //Free Mem
    cudaFree(deviceState);
    cudaFree(deviceSavedState);
    free(savedState);
    free(state);
}
