#include <stdio.h>
#include <stdlib.h>

#include <mpi.h>

int main(void)
{
  int lvlrequired, lvlprovided;

  lvlrequired = MPI_THREAD_MULTIPLE;

  MPI_Init_thread(NULL, NULL, lvlrequired, &lvlprovided);

  if (lvlprovided < lvlrequired)
    {
      printf("Required level of threading support *not* available\n");
    }
  else
    {
      printf("Required level of threading support *is* available\n");
    }

  MPI_Finalize();

  return(0);
}