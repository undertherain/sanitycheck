#include <mpi.h>
#include <iostream>
#include <chrono>
#include <thread>
#include <algorithm>

int main(const int argc, const char * argv[])
{
    MPI_Init(NULL, NULL);
    // std::cout<<"hi\n";
    const size_t size = 10000000;
    char* buf = new char[size];
    std::fill(buf, buf + size, 0);

    for (size_t i=0; i<100500; i++)
    {
        std::this_thread::sleep_for(std::chrono::seconds(1));
        for (size_t j=0; j<size; j++)
        {
            if (buf[j]!=0)
            std::cerr<<j;
        }

    }
    // std::cout<<"hi again\n";
    delete[] buf;
    return 0;
}
