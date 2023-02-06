import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributed.fsdp import FullyShardedDataParallel as FSDP


class MyModule(nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = nn.Linear(256, 256)
        self.l2 = nn.Linear(256, 2)

    def forward(self, x):
        h = self.l1(x)
        h = F.relu(h)
        h = self.l2(h)
        return h


# torch.cuda.set_device(device_id)
my_module = MyModule()
sharded_module = FSDP(my_module)
# sharded_module = my_module
optim = torch.optim.Adam(sharded_module.parameters(), lr=0.0001)
x = torch.rand(256)
logits = sharded_module(x)
print(logits)
loss = logits.sum()
loss.backward()
optim.step()
