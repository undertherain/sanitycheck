import torch

print("torch version", torch.__version__)
print("distr avail:\t", torch.distributed.is_available())
print("mpi avail:\t", torch.distributed.is_mpi_available())
print("nccl avail:\t", torch.distributed.is_nccl_available())
