check_cuda_aware: check_cuda_aware.c
	#export MPICH_CC=nvcc # if you use Mvapich
	export OMPI_CC=nvcc # if you use Open MPI
	#$(mpicc -show check_cuda_aware.c -arch sm_53 | sed -e 's/-Wl,/-Xlinker /g' | sed -e 's/-pthread/-Xcompiler -pthread/')
	nvcc check_cuda_aware.c -arch sm_53 -I/home/apps/kfc/mpi/openmpi/3.0.0/gcc/cuda9.1/include -Xcompiler -pthread -Xlinker -rpath -Xlinker /home/apps/kfc/mpi/openmpi/3.0.0/gcc/cuda9.1/lib -Xlinker --enable-new-dtags -L/home/apps/kfc/mpi/openmpi/3.0.0/gcc/cuda9.1/lib -lmpi


