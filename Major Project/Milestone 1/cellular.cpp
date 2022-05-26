#include <iostream>
#include <cstdlib>
#include <vector>
#include <iterator>
#include <unistd.h>
#include <fstream>
#include <chrono>
#include <string>

/**
*
*    Class Board:
*
*    Constructs an object that represents the gameboard.
*    Takes size as an initializer.
*
*    Requires: size is a positive, non zero integer
*    Ensures: construction of a game board (of size * size) using a 1D vector as an underlaying data structure 
*
*/
class Board
{
   
    private:
        /**
        *
        *   Private member variabels of the class.
        *
        *   rowSize: int that represents the size of the board's row
        *   ticksNo: int that represents the specified ticks the user wants the program to run for,
        *   currently only used for file naming purposes
        *   state: 1D vector that represents the game board
        *   FILE: const char* that contains the filepath to the output data
        *
        */
        int rowSize;
        int ticksNo;
        std::vector<int> state;
        std::string FILE;
    
    public:
        /**
        *
        *   Public constructor that sets up the inital member variables.
        *
        *   rowSize: set to the input size variable
        *   state: is resized to size*size and all variables are initalized to 0
        *   
        *   Removes FILE if it already exists then sets up an output stream to FILE.
        *   It then appends the rowSize to the top of the file and closes the stream.
        *
        */
        Board(int size, int ticks) {
            ticksNo = ticks;
            rowSize = size;
            FILE = std::string("data/") + "data_R=" + std::to_string(rowSize) + "_T=" + std::to_string(ticks) + ".txt";
            state.resize(size * size, 0);
            remove(FILE.c_str());
            std::ofstream output_file;
            output_file.open(FILE, std::ios_base::app);
            output_file << rowSize << "\n";
            output_file.close();
        }

        /**
        *   Initialises the state vector to a random spread of 1's and 0's
        *
        */
        void init_rand_state() {
            std::srand(10101010);
            for (auto iter = state.begin(); iter < state.end(); iter++) {
                *iter = std::rand() % 2;
            }
        }

        /**
        *   Initalises the state vector to data from a specified file
        *
        */
        void init_from_file(std::string name) {
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
        *   Performs a single tick which transforms the current state into the next state
        *
        */
        void tick() {
            std::vector<int> temp(rowSize * rowSize);

            for (auto iter = state.begin(); iter < state.end(); iter++) {
                int i = iter - state.begin();
                int x = i % rowSize;
                int y = i /rowSize;
                int num = num_neighbours(x, y);
                
                if ((num == 3 || num == 2) && cell_state(x, y) == 1) {
                    temp[i] = 1;
                } else if (num == 3 && cell_state(x, y) == 0) {
                    temp[i] = 1;
                } else {
                    temp[i] = 0;
                }
            }

            state = temp;
        }

        /**
        *   Prints the current state to the terminal
        *   Horrifically slow, use stream_to_board() unless 100% necessary
        *
        */
        void print_state() {

            for (auto iter = state.begin(); iter < state.end(); iter++) {
                int i = iter - state.begin();
                if (i % rowSize == 0) {
                    std::cerr << "\n";
                }
                if (*iter == 0) {
                    std::cerr << " ";
                } else {
                    std::cerr << ".";
                }
            }
            std::cerr << "\n";
        }

        /**
        *   Opens a file stream to FILE and streams the current state to that file
        *
        */
        void stream_to_file() {
            std::ofstream output_file;
            output_file.open(FILE, std::ios_base::app);
            for (const auto &e : state) output_file << e;
            output_file << "\n";
        }
    
    private:
        /**
        *   Returns the number of neighbours that a cell specified by int x and int y has
        *
        */
        int num_neighbours(int x, int y) {
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

            num += cell_state(xm1, y);
            num += cell_state(xp1, y);
            num += cell_state(x, ym1);
            num += cell_state(x, yp1);
            num += cell_state(xm1, ym1);
            num += cell_state(xp1, yp1);
            num += cell_state(xm1, yp1);
            num += cell_state(xp1, ym1);

            return num;
        }

        /**
        *   Returns the cell state at a given x and y
        *   For the purposes of translating 2D co-ords into 1D space 
        *
        */
        int cell_state(int x, int y) {
            return state[x + y*rowSize];
        }

};

int main(int argc, char** argv) {
    if (argc < 3) {
        std::cerr << "Usage: ./cellular{O level} {size} {ticks} {init file}" << std::endl;
        exit(0);
    }

    Board board(atoi(argv[1]), atoi(argv[2]));

    if (argc == 4) {
        board.init_from_file(argv[3]);
    } else {
        board.init_rand_state();
    }

    auto start = std::chrono::high_resolution_clock::now();

    int i;

    for (i = 0; i < int(atoi(argv[2])/4) * 4; i+=4) {
        board.stream_to_file();
        board.tick();
        board.stream_to_file();
        board.tick();
        board.stream_to_file();
        board.tick();
        board.stream_to_file();
        board.tick();
    }
    
    for (i; i < atoi(argv[2]); i++) {
        board.stream_to_file();
        board.tick();
    }

    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
    std::cout << "R=" << argv[1] << " T=" << argv[2] << " " << duration << "ms" << std::endl;

    return 0;
}