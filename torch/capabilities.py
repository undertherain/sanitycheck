import torch

print("torch version", torch.__version__)
print("cuda avail: ", torch.cuda.is_available())
print("distr avail:", torch.distributed.is_available())
print("mpi avail:  ", torch.distributed.is_mpi_available())
print("nccl avail: ", torch.distributed.is_nccl_available())
