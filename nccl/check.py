import chainermn
from chainermn import nccl
from mpi4py import MPI


def main():
    comm = chainermn.create_communicator("hierarchical")
    device = comm.intra_rank
    host = MPI.Get_processor_name()
    print(f"r {comm.rank} of {comm.size} [intra {comm.intra_rank} of {comm.intra_size}] on {host}")
    try:
        comm._init_comms()
    except:
        print(f"failed rank {comm.rank} intra {comm.intra_rank} of {comm.intra_size} on {host}")


if __name__ == "__main__":
    main()
