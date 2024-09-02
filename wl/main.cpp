#include <mpi.h>
#include <iostream>
#include <chrono>

int main(const int argc, const char * argv[])
{
    MPI_Init(NULL, NULL);
    std::cout<<"hi";
    std::this_thread::sleep_for(std::chrono::seconds(1));
    std::cout<<"hi again";
    return 0;
}
