import cffi
import chainer
from mpi4py import MPI
import numpy as np


def array_to_buffer_object(array):
    if chainer.cuda.get_array_module(array) is np:
        return array
    else:
        ffi = cffi.FFI()
        return (ffi.buffer(ffi.cast('void *', array.data.ptr), array.nbytes), MPI.FLOAT)


def main():
    comm = MPI.COMM_WORLD
    print("Hello! I'm rank %d from %d running in total..." % (comm.rank, comm.size))
    comm.Barrier()
    # test mpi bcast on numby array
    array = np.array([comm.rank] * 10, dtype=np.int32)
    if comm.rank == 1:
        print("array:", array)


if __name__ == "__main__":
    main()
