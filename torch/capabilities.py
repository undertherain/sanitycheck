import sys

import torch

print("python version:", sys.version_info)
print("running from  :", sys.executable)
print()
print("torch version : ", torch.__version__)
print()
print("cuda avail: ", torch.cuda.is_available())
print("distr avail:", torch.distributed.is_available())
print("mpi avail:  ", torch.distributed.is_mpi_available())
print("nccl avail: ", torch.distributed.is_nccl_available())
