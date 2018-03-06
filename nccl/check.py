import chainermn
from chainermn import nccl
from mpi4py import MPI


def main():
    comm = chainermn.create_communicator("pure_nccl")
    device = comm.intra_rank
    host = MPI.Get_processor_name()
    print(f"hi from r {comm.rank} of {comm.size} [intra {comm.intra_rank} of {comm.intra_size}] on {host}")
    try:
        comm._init_comms()
    except:
        print(f"FAILED r {comm.rank} of {comm.size} [intra {comm.intra_rank} of {comm.intra_size}] on {host}")
    comm.mpi_comm.Barrier()
    
    if comm.rank == 0:
        print("Done!")

if __name__ == "__main__":
    main()
