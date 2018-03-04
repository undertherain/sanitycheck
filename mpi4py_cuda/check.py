import cffi
import chainer
import chainermn
from mpi4py import MPI
import numpy as np
import cupy

SIZE = 10000


def array_to_buffer_object(array):
    if chainer.cuda.get_array_module(array) is np:
        return array
    else:
        ffi = cffi.FFI()
        return (ffi.buffer(ffi.cast('void *', array.data.ptr), array.nbytes), array.size, MPI.FLOAT)


def main():
    comm = chainermn.create_communicator("hierarchical")
    comm_mpi = comm.mpi_comm
    print(f"Rank {comm.rank} [mpi {comm_mpi.Get_rank()}], inner rank {comm.intra_rank} on {MPI.Get_processor_name()} from {comm.size} running in total..."  )
    comm_mpi.Barrier()
    # test mpi bcast on numby array
    array = np.array([comm.rank + 0.1] * SIZE, dtype=np.float32)
    if comm_mpi.rank == 1:
        print("cpu array before bcast:", array[:2])
    buf = array_to_buffer_object(array)
    comm_mpi.Bcast(buf)
    if comm_mpi.rank == 1:
        print("cpu array after bcast:", array[:2])

    comm_mpi.Barrier()

    array = cupy.array([comm_mpi.rank + 0.1] * SIZE, dtype=np.float32)
    if comm_mpi.rank == 1:
        print("gpu array before bcast:", array[:2])
    buf = array_to_buffer_object(array)
    if comm_mpi.rank == 1:
        print(f"created cffi buf, size = {len(buf[0])}, type={buf[2]}")
    comm_mpi.Bcast(buf)
    if comm_mpi.rank == 1:
        print("gpu array after bcast:", array[:2])
    comm_mpi.Bcast(buf)
    if comm_mpi.rank == 1:
        print("done!")


if __name__ == "__main__":
    main()
